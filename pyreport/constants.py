config_desc = (
    "# config option:  description <data type> \n"
    "# --------------------------------------- \n"
    "# twocolumn:      use two column mode <BOOL> \n"
    "# title:          the title of the paper <STRING> \n"
    "# author:         the aurthor of the paper <STRING> \n"
    "# email:          the correspondance email address <STRING> \n"
    "# affiliation:    the affiliation (eg. company/university) <STRING> \n"
    "# date:           the date of the paper (today if blank) <STRING> \n"
    "# abstract_file:  the name of the abstract in the output folder <FPATH> \n"
    "# keywords:       a list of keywords for this paper <LIST:STRING> \n"
    "# sections:       a list of sections files to be added to the paper <LIST:{FPATH,NAME}> \n"
    "# reference_file: the reference file if required <FPATH> \n"
    "# reference_type: the type of reference (apalike2 if blank) <STRING> \n"
)

default_config = {
    "twocolumn": False,
    "title": "Example title",
    "author": "John Smith",
    "email": "example@example.com",
    "affiliation": "Example Organisation",
    "date": None,
    "abstract_file": "abstract.tex",
    "keywords": [
        "keyword 1",
        "keyword 2",
        "keyword 3",
    ],
    "sections": [
        {"path": "introduction.tex", "name": "Introduction"},
        {"path": "methodology.tex", "name": "Methodology"},
        {"path": "results.tex", "name": "Results"},
        {"path": "discussion.tex", "name": "Discussion"},
    ],
    "reference_file": "refs.bib",
    "reference_type": None,
}

template_text = r"""\documentclass[a4paper, amsfonts, amssymb, amsmath,\BLOCK{ if twocolumn }twocolumn, \BLOCK{ endif } showkeys, nofootinbib, twoside]{revtex4-2}
\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[colorinlistoftodos, color=green!40, prependcaption]{todonotes}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{graphicx}

\graphicspath{ {./images/} }

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
 
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
 
\lstset{style=mystyle}

\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage[left=23mm,right=13mm,top=35mm,columnsep=15pt]{geometry} 
\usepackage{adjustbox}
\usepackage{placeins}
\usepackage[T1]{fontenc}
\usepackage{lipsum}
\usepackage{csquotes}
\usepackage[pdftex, pdftitle={Article}, pdfauthor={Author}]{hyperref}

\begin{document}

% insert title
\title{\VAR{ title }}

% insert author
\author{\VAR{ author }}

% insert email
\BLOCK{ if email }
\email[Correspondence email: ]{\VAR{ email }}
\BLOCK{ else }
\email[]{}
\BLOCK{ endif }

% insert affiliation
\BLOCK{ if affiliation }
\affiliation{\VAR{ affiliation }}
\BLOCK{ else }
\affiliation{}
\BLOCK{ endif }

% insert date
\BLOCK{ if date }
\date{\VAR{date}}
\BLOCK{ else }
\date{\today}
\BLOCK{ endif }

% insert abstract
\BLOCK{ if abstract_file }
\begin{abstract}
    \input{\VAR{ abstract_file }}
\end{abstract}
\BLOCK{ endif }

% insert keywords
\BLOCK{ if keywords }
\keywords{\BLOCK{ for keyword in keywords }\VAR{ keyword }\BLOCK{ if not loop.last }, \BLOCK{ endif }\BLOCK{ endfor }}
\BLOCK{ endif }

% create title
\maketitle

% insert sections
\BLOCK{ for section in sections }
\section{\VAR{ section.name }}
\input{\VAR{ section.path }}
\BLOCK{ endfor }

% insert references
\BLOCK{ if reference_file }
    \BLOCK{ if reference_type }
\bibliographystyle{\VAR{ reference_type }}
    \BLOCK{ else }
\bibliographystyle{apalike2}
    \BLOCK{ endif }
\bibliography{\VAR{ reference_file }}
\BLOCK{ endif }

\end{document}
"""
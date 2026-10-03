\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{l4dc2022}[2022/04/01 v2.0 L4DC 2022 Proceedings]

\@ifundefined{ifanonsubmission}{
  \newif\ifanonsubmission
  \anonsubmissionfalse
}{}

\@ifundefined{iffinalsubmission}{
  \newif\iffinalsubmission
  \finalsubmissionfalse
}{}

\DeclareOption{anon}{\anonsubmissiontrue}
\DeclareOption{final}{\finalsubmissiontrue}
\ProcessOptions\relax

\LoadClass[pmlr]{jmlr}

% % L4DC 
% \jmlrvolume{vol 168}
% \jmlryear{2022}
% \jmlrproceedings{PMLR}{Proceedings of Machine Learning Research}
% Arxiv
\jmlrvolume{}
\jmlryear{}
\jmlrproceedings{PMLR}{}

\iffinalsubmission
  \editors{R. Firoozi, N. Mehr, E. Yel, R. Antonova, J. Bohg, M. Schwager, M. Kochenderfer}
  \jmlrworkshop{4th Annual Conference on Learning for Dynamics and Control}
\fi

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Temporary workaround fixing issues with \includegraphics (concerns LaTeX2e
%% releases after October 2019) [jsieber; 2020-11-12]
\def\set@curr@file#1{\def\@curr@file{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

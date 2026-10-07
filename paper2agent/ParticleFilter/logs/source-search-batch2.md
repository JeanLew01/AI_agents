# Source search: batch 2 (10 papers)

Date: 2026-10-05. I used only legal sources: arXiv, HAL/INRIA, Strathprints, Lancaster EPrints, author pages and publisher open access. I did not log in anywhere and did not use any shadow library.
I checked every saved file with `pdfinfo` and the first-page text from `pdftotext`. All files are in `papers/`. Checksums were appended to `papers/SHA256SUMS`, and `sha256sum -c` passes.

## Summary

| # | Key | Status | Version | Pages | Code |
|---|-----|--------|---------|-------|------|
| 1 | benavoli-piga-2016 | downloaded + TeX | arXiv v2 preprint | 20 | none found |
| 2 | greco-vasile-2022 | downloaded | accepted author manuscript (Strathprints) | 44 | none found |
| 3 | abdallah-box-pf-2008 | **not found legally** | none | none | third-party only |
| 4 | combastel-ezgkf-2016 | **not found legally** | none | none | none found |
| 5 | raices-cruz-robust-is-mcmc-2022 | downloaded + TeX | arXiv v1 preprint (the CC BY publisher version exists but could not be fetched by script) | 19 | official R/Stan repo |
| 6 | andrieu-pmcmc-2010 | downloaded | journal-typeset version on the author's page, **with discussion and reply** | 74 | none official |
| 7 | legland-oudjane-2003 | downloaded | INRIA RR-4431 (2002) | 29 | none found |
| 8 | benavoli-lower-previsions-2011 | downloaded | author manuscript (Oct 2010) | 15 | none found |
| 9 | gning-box-bernoulli-2012 | downloaded | author manuscript, revision 2 (Lancaster) | 15 | none found |
| 10 | haj-chhade-box-messages-2014 | downloaded | publisher OA version (CC BY 4.0) | 24 | none found |

## Per paper

### 1. Benavoli & Piga (2016): benavoli-piga-2016.pdf
- Published as: A. Benavoli, D. Piga, "A probabilistic interpretation of set-membership filtering: Application to polynomial systems through polytopic bounding", *Automatica* 70:158–172, Aug 2016. DOI 10.1016/j.automatica.2016.03.021
- Status: downloaded. URL: https://arxiv.org/pdf/1505.01034 (v2). TeX source from https://arxiv.org/e-print/1505.01034, extracted to `tex-source/benavoli-piga-2016/` (main file `FilteringSM_v15.tex`, EPS figures).
- Version: arXiv v2 preprint dated 12 Apr 2016. This is after the paper was accepted (Mar 2016), so it is close to the accepted manuscript but it is not the Elsevier-typeset version. Pages: 20.
- Differences: none of substance are known. The author page also has `FilteringSM_v15` (http://www.idsia.ch/~alessio/benavoli2016a.pdf, 6 Mar 2016, 19 pp). The arXiv v2 text is that file plus about one extra sentence and small hyphenation changes, so arXiv v2 is the later of the two.
- Code: none found (searched GitHub and the author's software page).

### 2. Greco & Vasile (2022): greco-vasile-2022.pdf
- Published as: C. Greco, M. Vasile, "Robust Bayesian Particle Filter for Space Object Tracking Under Severe Uncertainty", *J. Guidance, Control, and Dynamics* 45(3):481–498, Mar 2022. DOI 10.2514/1.G006157
- Status: downloaded. URL: https://strathprints.strath.ac.uk/78148/7/Greco_Vasile_JGCD_2021_Robust_Bayesian_particle_filter_for_space_object_tracking_under_severe_uncertainty.pdf (record https://strathprints.strath.ac.uk/78148)
- Version: accepted author manuscript (accepted 3 Oct 2021), Strathprints licence 1.0. Single-column LaTeX layout. Pages: 44 (the journal version is 18 pages).
- Differences: this is the AIAA-accepted text without AIAA copy-editing or typesetting. There is a related, different earlier conference paper: "Robust particle filter for space objects tracking under severe uncertainty" (AAS/AIAA 2019, Strathprints 70566). Do not confuse the two.
- Code: none found.

### 3. Abdallah, Gning, Bonnifait (2008): NOT FOUND LEGALLY
- Published as: F. Abdallah, A. Gning, P. Bonnifait, "Box particle filtering for nonlinear state estimation using interval analysis", *Automatica* 44(3):807–815, Mar 2008. DOI 10.1016/j.automatica.2007.07.024
- Publisher URL for library download: https://doi.org/10.1016/j.automatica.2007.07.024 (https://www.sciencedirect.com/science/article/pii/S0005109807003731)
- Where I looked: HAL API (no record), Unpaywall, OpenAlex and Semantic Scholar (all "closed"), Lancaster EPrints, the LISER Pure record (metadata only), and Google-style searches. The UTC/Heudiasyc author pages (hds.utc.fr/~bonnifai, ~fabdalla) returned HTTP 403.
- Legal open substitutes on the same method, which I did not download: Gning, Ristic, Mihaylova, Abdallah, "An Introduction to Box Particle Filtering", IEEE SPM 2013 (Lancaster EPrints 53537); A. Gning's PhD thesis, tel-00158375 (theses.hal.science).
- Code: no official code. Third-party MATLAB: https://github.com/evbernardes/BoxParticleFilter (no licence file).

### 4. Combastel (2016): NOT FOUND LEGALLY
- Published as: C. Combastel, "An Extended Zonotopic and Gaussian Kalman Filter (EZGKF) merging set-membership and stochastic paradigms: Toward non-linear filtering and fault detection", *Annual Reviews in Control* 42:232–243, 2016. DOI 10.1016/j.arcontrol.2016.07.002. The page range is 232–243 per Crossref.
- Publisher URL for library download: https://doi.org/10.1016/j.arcontrol.2016.07.002
- Where I looked: HAL hal-01650603 is a metadata-only notice with no file. Unpaywall, OpenAlex and Semantic Scholar all report "closed". I found no arXiv version (the author's arXiv papers start in 2020) and no author-page PDF.
- Code: none found.

### 5. Raices Cruz, Lindström, Troffaes, Sahlin (2022): raices-cruz-robust-is-mcmc-2022.pdf
- Published as: I. Raices Cruz, J. Lindström, M.C.M. Troffaes, U. Sahlin, "Iterative importance sampling with Markov chain Monte Carlo sampling in robust Bayesian analysis", *Computational Statistics & Data Analysis* 176:107558, Dec 2022. DOI 10.1016/j.csda.2022.107558
- Status: downloaded. URL: https://arxiv.org/pdf/2206.08728 (v1, the only version). TeX source extracted to `tex-source/raices-cruz-robust-is-mcmc-2022/` (`article-arxiv.tex`, `.bbl`, PDF figures).
- Version: arXiv v1 preprint, 17 Jun 2022. Pages: 19.
- Differences: the published article is open access under CC BY 4.0 (hybrid OA). The links are https://www.sciencedirect.com/science/article/pii/S0167947322001384 and the Durham VoR https://durham-repository.worktribe.com/preview/1202609/36195VoR.pdf. Both sites returned a JavaScript/Cloudflare bot challenge to curl, so I could not save that version. **The user can download the CC BY VoR for free in a browser.** The arXiv v1 is the preprint and may lack final revisions and copy-editing.
- Code: https://github.com/Iraices/IIS_MCMC is the official R/Stan code for this paper (per the README). It has no licence file.

### 6. Andrieu, Doucet, Holenstein (2010): andrieu-pmcmc-2010.pdf
- Published as: C. Andrieu, A. Doucet, R. Holenstein, "Particle Markov chain Monte Carlo methods", *JRSS Series B* 72(3):269–342, 2010. DOI 10.1111/j.1467-9868.2009.00736.x
- Status: downloaded. URL: https://www.stats.ox.ac.uk/~doucet/andrieu_doucet_holenstein_PMCMC.pdf (A. Doucet's Oxford page).
- Version: the journal-typeset PDF (header "J. R. Statist. Soc. B (2010) 72, Part 3, pp. 269–342"), posted by the author. Pages: 74, covering the full journal range pp. 269–342.
- **It includes the discussion and the reply.** The read paper and its appendices come first. The discussion contributions start on p. 302 ("Discussion on the Paper by Andrieu, Doucet and Holenstein"). Then come "The authors replied later, in writing, as follows", and "References in the discussion" at the end.
- Code: no official code. PMCMC (PMMH and particle Gibbs) is implemented in third-party libraries, for example https://github.com/nchopin/particles (MIT).

### 7. Le Gland & Oudjane (2003): legland-oudjane-2003.pdf
- Published as: F. Le Gland, N. Oudjane, "A robustification approach to stability and to uniform particle approximation of nonlinear filters: the example of pseudo-mixing signals", *Stochastic Processes and their Applications* 106(2):279–316, Aug 2003. DOI 10.1016/S0304-4149(03)00041-3
- Status: downloaded. URL: https://inria.hal.science/inria-00072157/file/RR-4431.pdf (HAL inria-00072157). HAL's Anubis check blocks browser user agents, so the download needed a non-browser user agent.
- Version: INRIA research report RR-4431, March 2002, with the same title. Pages: 29. The journal version is 38 pages long, but the page counts are not comparable because the report uses INRIA's own layout.
- Differences: this is a pre-publication research report, and there may be editorial or refereeing changes before the SPA version that I have not checked.
- **Caveat:** the PDF uses bitmap Type-3 fonts (old dvips output), so `pdftotext` returns garbage. Building a reading package will need OCR or page images.
- The publisher version is free: Elsevier "open archive" (bronze OA) at https://www.sciencedirect.com/science/article/pii/S0304414903000413. It has clean text, but ScienceDirect blocked the scripted download. **The user can save it in a browser and should prefer it over RR-4431.**
- Code: none found.

### 8. Benavoli, Zaffalon, Miranda (2011): benavoli-lower-previsions-2011.pdf
- Published as: A. Benavoli, M. Zaffalon, E. Miranda, "Robust Filtering Through Coherent Lower Previsions", *IEEE Trans. Automatic Control* 56(7):1567–1581, Jul 2011. DOI 10.1109/TAC.2010.2090707
- Status: downloaded. URL: http://www.idsia.ch/~alessio/IP_filtering.pdf, which is linked from https://alessiobenavoli.com/research/filtering-and-control-with-set-of-distributions/
- Version: the author's manuscript in two-column IEEE draft layout, with PDF date 28 Oct 2010, around the time of IEEE early access. It is most likely the accepted version. Pages: 15, matching the 15 journal pages.
- Differences: none known apart from IEEE copy-editing and typesetting. The Univ. Oviedo repository record (hdl 10651/9834) has no file attached.
- Code: none found.

### 9. Gning, Ristic, Mihaylova (2012): gning-box-bernoulli-2012.pdf
- Published as: A. Gning, B. Ristic, L. Mihaylova, "Bernoulli Particle/Box-Particle Filters for Detection and Tracking in the Presence of Triple Measurement Uncertainty", *IEEE Trans. Signal Processing* 60(5):2138–2151, May 2012. DOI 10.1109/TSP.2012.2184538
- Status: downloaded. URL: https://eprints.lancs.ac.uk/id/eprint/52300/1/Bernouli_Box_PF.pdf (record https://eprints.lancs.ac.uk/id/eprint/52300/)
- Version: author manuscript "manuscrit_Rev.2" (second revision, 28 Dec 2011), posted under IEEE's personal-use notice. Pages: 15.
- Differences: this is the final revision before publication, without IEEE typesetting. The White Rose record 82267 has no file. A related but different conference paper is the FUSION 2011 Box-PF paper (Lancaster 53141).
- Code: none found.

### 10. Haj Chhadé et al. (2014): haj-chhade-box-messages-2014.pdf
- **Metadata corrections:** the venue is *Mathematics in Computer Science* 8(3–4):455–478 (Springer, published online 7 Aug 2014), **not** *Mathematical Problems in Engineering*. The authors are H. Haj Chhadé, A. Gning, F. Abdallah, I. Mougharbel, S. Julier. **Mihaylova is not an author**, and the author order differs from the one in the request. DOI 10.1007/s11786-014-0200-2
- Status: downloaded. URL: https://link.springer.com/content/pdf/10.1007/s11786-014-0200-2.pdf
- Version: the publisher's open-access version, CC BY 4.0. Pages: 24, matching the journal pages.
- Code: none found.

## Notes
- Two legal free versions exist but could not be fetched by script because of bot protection: CSDA paper 5 (CC BY version) and SPA paper 7 (Elsevier open archive). They are worth fetching manually because they are better than the versions saved here.
- HAL was reached through its public search API and direct file URLs. Unpaywall, OpenAlex, Crossref and Semantic Scholar were queried for metadata and OA status only.

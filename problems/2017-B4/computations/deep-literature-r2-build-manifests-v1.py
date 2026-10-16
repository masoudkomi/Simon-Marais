#!/usr/bin/env python3
"""Record owned literature sources, observed access limits and retained queries.
No mathematical computation or web request. Full papers stay in ignored cache.
Run from repository root; reads cached sources and writes only owned new prefixes.
"""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CACHE = '.cache/literature/deep-literature-r2/'
DATE = '2026-10-16'


def cached(name, url, version, read_scope, pages=None):
    p = ROOT / (CACHE + name)
    return {
        'url': url, 'version': version, 'checked_utc_date': DATE,
        'cache_path': str(p.relative_to(ROOT)),
        'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        'bytes': p.stat().st_size, 'pdf_pages': pages,
        'read_scope': read_scope,
        'distribution': 'local ignored cache only; no redistribution permission inferred',
    }


def existing(path, url, read_scope, version):
    p = ROOT / path
    return {
        'url': url, 'version': version, 'checked_utc_date': DATE,
        'cache_path': path, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        'bytes': p.stat().st_size, 'read_scope': read_scope,
        'distribution': 'pre-existing ignored cache only',
    }


def web_only(url, result, version=None):
    return {'url': url, 'checked_utc_date': DATE, 'version': version,
            'result': result, 'cache_path': None, 'sha256': None,
            'hash_limit': 'no downloaded original bytes; no hash invented'}


def query(q, outcome):
    return {'searched_utc_date': DATE, 'query': q, 'outcome': outcome}


sources17 = [
    cached('2017-ckdfs-2402.13107v2.pdf', 'https://arxiv.org/pdf/2402.13107v2',
           'arXiv v2, 2024-03-21; SoCG 2024 DOI 10.4230/LIPIcs.SoCG.2024.43',
           'Full main text, constructions, Sections 5.1/5.2/6 and reduction inspected; source computations not rerun', 19),
    cached('2017-dallant-zone-2502.20909v2.pdf', 'https://arxiv.org/pdf/2502.20909v2',
           'arXiv v2, 2025-03-07; current record rechecked',
           'All sections inspected; Lemmas 3-7 and exact domain reconstructed into separately frozen unverified candidate', 12),
    cached('2017-dallant-lower-2402.13923v1.pdf', 'https://arxiv.org/pdf/2402.13923v1',
           'arXiv v1, 2024-02-21; merged/superseded lower-bound result',
           'Full text cached and extracted; selected introduction/method sections inspected, not a full independent audit', 23),
    cached('2017-destainville-octagonal-0004145v2.pdf', 'https://arxiv.org/pdf/cond-mat/0004145v2',
           'arXiv v2, 2000-08-25',
           'Definitions, de Bruijn/tiling dictionary, Sections 2.2/3.2/3.3, additive polynomial, entropy/boundary caveats inspected'),
    cached('2017-zerbib-zone-vertex-1604.07268v1.pdf', 'https://arxiv.org/pdf/1604.07268v1',
           'arXiv v1 record 2016-04-25; cached compilation dateline 2018-08-27; SIAM journal 2011 DOI 10.1137/100787246',
           'Theorems 1/2, line/vertex conventions, discharging proof and tight-example scope inspected', 13),
    web_only('https://arxiv.org/abs/2502.20909', 'Current version remains v2; explicit v1 correction removes n-u<=m from Lemma 3'),
    web_only('https://arxiv.org/abs/2402.13107', 'Current version v2; merged independent submissions; publication/version dates checked'),
    web_only('https://github.com/fcorteskuehnast/counting-arrangements', 'Author supplemental repository inspected; MIT license, small configuration and LGV script located; not executed'),
    web_only('https://scheucher.dev/', 'Current author page inspected; same lower-bound paper located; unrelated 2026 papers not treated as count improvements'),
    web_only('https://justindallant.com/', 'Current author publication page inspected; no stronger relevant count result located'),
    web_only('https://page.mi.fu-berlin.de/rote/Papers/slides/Oswinfest-2026-Enumeration%2Band%2BCounting%2Bof%2BPseudoline%2BArrangements.pdf',
             '167-page primary talk PDF accessible through web tool; pp.18-41 rope/partial-arrangement algorithm and finite C(16) inspected. Normal curl failed twice: 45s and 30s external caps, exit 28, sessions 30769/47562 reaped. No local original bytes.',
             'Oswinfest, 2026-03-28; talk date does not establish enumeration date'),
    web_only('https://epubs.siam.org/doi/abs/10.1137/100787246', 'Primary journal confirms 2011 publication, straight lines/general position, pp.719-730'),
    web_only('https://www2.math.technion.ac.il/~room/ps_files/zonespl.pdf', 'Optional backward-reference web request plus title search did not return before bounded follow-up ended; functions cell 93 terminated. No original zone manuscript obtained or theorem attributed to an unread full text.'),
    existing('.cache/official/2017-solutions.pdf', 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf',
             'B4 context/counting convention only, p12; no other problems investigated', 'Official2017 notes'),
]
queries17 = [
    query('"number of pseudoline arrangements" "2026" bound 0.649', 'Located2026Rote slides and current author references; no new asymptotic theorem located'),
    query('"pseudoline arrangements" "concavity" Dallant', 'No direct prior concavity reduction located; not a novelty proof'),
    query('"On the zone complexity of a vertex" Zerbib SIAM 2011 719 730', 'Primary SIAM record/author site verify2011 despite later arXiv posting'),
]

sources18 = [
    cached('2018-hering-howard-author-2014.pdf', 'https://webhomes.maths.ed.ac.uk/~mhering/HH.pdf',
           'Author preprint dated2014-01-19, arXiv1211.3941v2; journal2014 DOI10.1007/s00209-013-1272-4',
           'Theorem1.1/1.2, Proposition3.2 full proof, relevant Sections2/4/5 and Remarks3.6/3.7 inspected', 19),
    existing('.cache/literature/2018/review-2/ottaviani.pdf', 'https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf',
             'Theorem40 printedp186/PDFp68, parity/grading conventions and attribution to Howe inspected; source PDF only, no peer review conclusion used',
             'Rend.Sem.Mat.71(2013),119-194; arXiv1305.2749'),
    cached('2018-henderson-gazette-mar2019.pdf', 'https://austms.org.au/wp-content/uploads/2025/02/Mar19-461.pdf',
           'Gazette46(1),March2019, articleprintedpp33-34',
           'Full issue cached; B4 paragraph onPDFp36/printedp34 directly extracted; webOCR shape error not adopted', 84),
    existing('.cache/official/2018-solutions.pdf', 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf',
             'Only B4 general-context commentspp16-17 used; preliminary case not researched/reproduced', 'Official2018 notes'),
    web_only('https://www.ams.org/books/pspum/048/', 'Normal publisher request failed/403; original Howe chapter not read'),
    web_only('https://doi.org/10.1090/pspum/048/974333', 'Normal DOI/publisher route failed; no full original Howe theorem claimed'),
    web_only('https://arxiv.org/abs/1211.3941', 'Version/date checked against authorPDF and existing verified references', 'v2,2014-01-19'),
]
queries18 = [
    query('"Howe" "The classical groups and invariants of binary forms" pdf', 'Located citations/AMS metadata; no legal full original obtained'),
    query('"Simon Marais" "2018" "B4" "Hering"', 'No official explanation/correction of historical open-label discrepancy located'),
    query('"Kostka" "2018 Simon Marais" explicit formula', 'Located contemporaryHenderson report; originalPDF confirms exact target'),
]

sources24 = [
    cached('2024-mcguire-thesis-1995.pdf', 'https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf',
           'CaltechPhD1995, DOI10.7907/1CZ2-6S05',
           'ScannedPDF; visually inspectedPDFpp4-7,11-16,18-38; exactg_t definition, original-authorJMW correspondence, fullThm2.1prime/6/7/8 proofs, Proposition9. Not all97pages or laterchapter proofs audited.', 97),
    cached('2024-delgado-janwa-1612.05997v1.pdf', 'https://arxiv.org/pdf/1612.05997v1',
           'arXivv1,2016-12-18',
           'Full definitions and Section3 eq5/6, statedcomponentfields/specialization; perturbation scope distinguished from puremonomialtarget', 14),
    cached('2024-delgado-janwa-fermat-cn232.pdf', 'https://combinatorialpress.com/article/cn/Volume%20232/vol-232-paper%204.pdf',
           'CongressusNumerantium232(2019), advertisedpp101-112',
           'All10scannedPDFpages visually inspected; printedpages101,102,104-111, so scan omits103 and advertised112. Not a complete theorem-proof source.', 10),
    cached('2024-ferard-sequel-hal-api.json', 'https://api.archives-ouvertes.fr/search/?q=halId_s:hal-03417811&fl=title_s,uri_s,fileMain_s,openAccess_bool,docType_s,linkExtUrl_s,doiId_s,version_i&wt=json',
           'NormalpublicHALAPI queried2026-10-16; recordv1',
           'numFound1, openAccess_boolfalse, nofileMain; metadataonly'),
    existing('.cache/official/2024-solutions.pdf', 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc_2024_solutions.pdf',
             'B4headingPDFp15/printedp14 explicitPeterMcNamara; partb domains/nonconstantmod2 requirement; preliminary proof not reproduced', 'Official2024 solutions'),
    web_only('https://thesis.caltech.edu/4053/', 'Public original-author thesis record, degree/year/DOI/filelink verified'),
    web_only('https://authors.library.caltech.edu/records/wcxdz-pkj80', 'JW1993record explicitlymetadata-only, noPDFdownload'),
    web_only('https://link.springer.com/chapter/10.1007/3-540-56686-4_43', 'Subscriptionpreview expresslylabelled; full1993chapter not obtained; online2005metadata not publicationyear'),
    web_only('https://www.sciencedirect.com/science/article/pii/S0021869385713725', 'Normaljournalpage unavailable; JMW1995originaljournalPDFnotread, originalauthorparallelthesisobtained'),
    web_only('https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497', 'Primaryabstractonly; fullqualificationsnotverified; normalPDFnavigationaccesslimitrespected', 'Férard2014'),
    web_only('https://gaati.org/publications/fr/', 'PrimarylabpublicationlistidentifiesHAL01779804,03417811,03417866; noindividualsetterinference'),
    web_only('https://gaati.org/ferard/', 'Normalprospectiveauthorpage request internalerror; noaccessworkaround'),
    web_only('https://hal.science/hal-01779804', 'Normalrecordanti-bot/error; priornormalAPIopenaccessflagwithoutfileMain; /document404. Fulltextnotobtained'),
    web_only('https://doi.org/10.1007/s12095-017-0213-1', 'Sequelabstractmetadataonly; exactthreshold/excludedformsunread', 'Férard2017II'),
    web_only('https://doi.org/10.1090/conm/686/13777', 'Distinct2017Kasamiperturbationpaper identifiedthroughreferences; fulltextnotinspected'),
]
queries24 = [
    query('Gary McGuire 1995 thesis Absolutely Irreducible Curves Applications Combinatorics Coding Theory Caltech thesis', 'Locatedlegalfulloriginalauthorthesis, downloadedandvisuallyreadrelevanttheorems'),
    query('Janwa Wilson 1993 Hyperplane sections Fermat varieties odd characteristic two download author pdf', 'Caltechmetadataonly/Springersubscriptionpreview; nofulloriginal'),
    query('Férard Rodier 2014 irreducibility multivariate polynomials differential cryptanalysis t 5 modulo 8 13', 'Primaryabstractandlatercitations, nofullpremise'),
    query('"Férard" "hyperplane sections" "2014" pdf', 'Publisher/lab/metadata routes; originalfulltextstillunobtained'),
    query('"Férard" "Fermat varieties" "II" pdf', 'Distinct2017sequel/HALrecord; APIshowsclosedmetadata'),
    query('"On the irreducibility" "Férard" "pdf" -site:researchgate.net -site:aimsciences.org -site:dblp.org -site:dblp.dagstuhl.de -site:scispace.com', 'Noadditionalverifiedlegalfulltextlocated'),
]


def main():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    for year, sources, queries in [(2017,sources17,queries17),(2018,sources18,queries18),(2024,sources24,queries24)]:
        p = ROOT / f'problems/{year}-B4/notes/deep-literature-r2-search-sources-v1.json'
        p.parent.mkdir(parents=True, exist_ok=True)
        images = sorted((ROOT / CACHE).glob(f'{year}-*.png'))
        extracted = sorted((ROOT / CACHE).glob(f'{year}-*.txt'))
        record = {
            'recorded_utc': now, 'checked_utc_date': DATE,
            'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
            'effective_settings_readback': 'unavailable',
            'scope': 'entire2017B4' if year==2017 else ('general2018enumeration, no m5 research' if year==2018 else '2024B4partb only'),
            'status': 'literature/research checkpoint; all new deductions candidate proof - unverified',
            'sources': sources, 'queries_exact_text_retained': queries,
            'query_log_limit': 'Exact retained search strings and source-opening routes are recorded. Earlier discovery traffic summarized in the report is not reconstructed into invented exact search events.',
            'derived_cache_files': [
                {'path':str(x.relative_to(ROOT)), 'sha256':hashlib.sha256(x.read_bytes()).hexdigest(), 'bytes':x.stat().st_size,
                 'kind':'locally derived page render or extraction; not an independent source'} for x in images+extracted],
            'access_policy': 'Normal public sources only; no charges, login, author contact, CAPTCHA/bot challenge solution or access bypass. Full third-party files remain ignored .cache/.',
            'cache_ignore_evidence': '.gitignore contains .cache/ and *.pdf',
            'telemetry': {'primary_used_percent':15, 'window_minutes':10080, 'resets_at':1792745187, 'cutoff_total_used_percent':90},
            'no_shared_edits': True, 'no_git_actions': True,
        }
        p.write_text(json.dumps(record, indent=2, ensure_ascii=False)+'\n')
        print(json.dumps({'path':str(p.relative_to(ROOT)), 'sources':len(sources), 'queries':len(queries),
                          'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()

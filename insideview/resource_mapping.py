# coding: utf-8

RESOURCE_MAPPING = {
    'target_company_list': {
        'resource': '/target/companies',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/204395607--POST-Contact-List'
    },
    'target_company_lookup': {
        'resource': '/target/company/lookup',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/209198069--POST-Company-Lookup'
    },
    'target_new_company_details': {
        'resource': '/target/companies/{new_company_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/203440578--GET-New-Company-Details'
    },
    'target_contact_lookup': {
        'resource': '/target/company/{company_id}/contacts',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202798443--GET-Contact-Lookup'
    },
    'target_contact_list': {
        'resource': '/target/contacts',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/204395607--POST-Contact-List'
    },
    'target_new_contact_details': {
        'resource': '/target/contact/{new_contact_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202798453--GET-New-Contact-Details'
    },
    'enrich': {
        'resource': '/enrich',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202773253--POST-Enrich'
    },
    'enrich_job': {
        'resource': '/enrich/job',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202693176--POST-Enrich-Job'
    },
    'enrich_job_status': {
        'resource' : '/enrich/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202693186--GET-Enrich-Job-Status',
    },
    'enrich_job_cancel': {
        'resource' : '/enrich/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202693186--GET-Enrich-Job-Status',
    },
    'enrich_job_results': {
        'resource': '/enrich/job/{job_id}/results',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202773213--GET-Enrich-Job-Results',
    },
}

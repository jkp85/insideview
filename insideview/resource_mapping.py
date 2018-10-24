# coding: utf-8

RESOURCE_MAPPING = {
    'target_company_list': {
        'resource': '/target/companies',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/203433468--POST-Company-List'
    },
    'target_new_company_details': {
        'resource': '/target/companies/{new_company_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/203440578--GET-New-Company-Details'
    },
    'target_company_list_build_job': {
        'resource': '/target/companies/export/job',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/228174088--POST-Asynchronous-batch-Target-Company-List-Build-API'
    },
    'target_company_list_build_job_status': {
        'resource' : '/target/companies/export/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/227962467--GET-Asynchronous-batch-Target-Company-List-Build-status-API-',
    },
    'target_company_job_cancel': {
        'resource' : '/target/companies/export/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/228174128--DELETE-Cancel-Asynchronous-batch-Target-Company-List-Build-Job',
    },
    'target_company_job_results': {
        'resource': '/target/companies/export/job/{job_id}/results',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/228174208--GET-Asynchronous-batch-Target-Company-List-Build-Results',
    },
    'target_contact_list': {
        'resource': '/target/contacts',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/204395607--POST-Contact-List'
    },
    'target_new_contact_details': {
        'resource': '/target/contact/{new_contact_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202798453--GET-New-Contact-Details'
    },
    'target_contact_list_build_job': {
        'resource': '/target/contacts/export/job',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/235486227--POST-Asynchronous-batch-Target-Contact-List-Build-API'
    },
    'target_contact_list_build_job_status': {
        'resource' : '/target/contact/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/203638968--GET-New-Contact-Details-Job-Status',
    },
    'target_contact_list_build_job_cancel': {
        'resource' : '/target/contact/job/{job_id}',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/204395617--DELETE-Cancel-New-Contact-Details-Job',
    },
    'target_contact_list_build_job_results': {
        'resource': '/target/contact/job/{job_id}/results',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/203638978--GET-New-Contact-Details-Job-Results',
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
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202693206--DELETE-Cancel-Enrich-Job',
    },
    'enrich_job_results': {
        'resource': '/enrich/job/{job_id}/results',
        'docs': 'https://kb.insideview.com/hc/en-us/articles/202773213--GET-Enrich-Job-Results',
    },
}

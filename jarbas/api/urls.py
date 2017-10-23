from django.conf.urls import url

from jarbas.api.views import (
    ApplicantListView,
    CompanyDetailView,
    ReceiptDetailView,
    ReimbursementDetailView,
    ReimbursementListView,
    SameDayReimbursementListView,
    SubquotaListView,
)


urlpatterns = [
    url(
        r'^chamber_of_deputies/reimbursement/$',
        ReimbursementListView.as_view(),
        name='reimbursement-list'
    ),
    url(
        r'^chamber_of_deputies/reimbursement/(?P<document_id>\d+)/$',
        ReimbursementDetailView.as_view(),
        name='reimbursement-detail'
    ),
    url(
        r'^chamber_of_deputies/reimbursement/(?P<document_id>\d+)/receipt/$',
        ReceiptDetailView.as_view(),
        name='reimbursement-receipt'
    ),
    url(
        r'^chamber_of_deputies/reimbursement/(?P<document_id>\d+)/same_day/$',
        SameDayReimbursementListView.as_view(),
        name='reimbursement-same-day'
    ),
    url(
        r'^company/(?P<cnpj>\d{14})/$',
        CompanyDetailView.as_view(),
        name='company-detail'
    ),
    url(r'^chamber_of_deputies/applicant/$', ApplicantListView.as_view(), name='applicant-list'),
    url(r'^chamber_of_deputies/subquota/$', SubquotaListView.as_view(), name='subquota-list')
]

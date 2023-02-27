from flask import Blueprint, render_template
from mimesis import Text

report = Blueprint(
    'report',
    __name__,
    static_folder='../static',
    url_prefix='/reports'
)

REPORTS = [
    Text().sentence(),
    Text().sentence(),
    Text().sentence(),
    Text().sentence(),
    Text().sentence()
]


@report.route('/')
def report_list():
    return render_template(
        'reports/list.html',
        reports=REPORTS,
    )

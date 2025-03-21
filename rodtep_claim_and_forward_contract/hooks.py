app_name = "rodtep_claim_and_forward_contract"
app_title = "Rodtep Claim And Forward Contract"
app_publisher = "sf"
app_description = "sfsd"
app_email = "contact@erpdata.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "rodtep_claim_and_forward_contract",
# 		"logo": "/assets/rodtep_claim_and_forward_contract/logo.png",
# 		"title": "Rodtep Claim And Forward Contract",
# 		"route": "/rodtep_claim_and_forward_contract",
# 		"has_permission": "rodtep_claim_and_forward_contract.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rodtep_claim_and_forward_contract/css/rodtep_claim_and_forward_contract.css"
# app_include_js = "/assets/rodtep_claim_and_forward_contract/js/rodtep_claim_and_forward_contract.js"

# include js, css files in header of web template
# web_include_css = "/assets/rodtep_claim_and_forward_contract/css/rodtep_claim_and_forward_contract.css"
# web_include_js = "/assets/rodtep_claim_and_forward_contract/js/rodtep_claim_and_forward_contract.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rodtep_claim_and_forward_contract/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
        "Payment Entry": "public/js/doctype_js/payment_entry.js",
        "Sales Invoice": "public/js/doctype_js/sales_invoice.js",
    "Journal Entry": "public/js/doctype_js/journal_entry.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "rodtep_claim_and_forward_contract/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "rodtep_claim_and_forward_contract.utils.jinja_methods",
# 	"filters": "rodtep_claim_and_forward_contract.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rodtep_claim_and_forward_contract.install.before_install"
# after_install = "rodtep_claim_and_forward_contract.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rodtep_claim_and_forward_contract.uninstall.before_uninstall"
# after_uninstall = "rodtep_claim_and_forward_contract.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "rodtep_claim_and_forward_contract.utils.before_app_install"
# after_app_install = "rodtep_claim_and_forward_contract.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "rodtep_claim_and_forward_contract.utils.before_app_uninstall"
# after_app_uninstall = "rodtep_claim_and_forward_contract.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rodtep_claim_and_forward_contract.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
        "Payment Entry": {
                "on_submit": "rodtep_claim_and_forward_contract.api.pe_on_submit",
                "before_cancel": "rodtep_claim_and_forward_contract.api.pe_on_cancel",
        },
        "Journal Entry": {
            "on_cancel": "rodtep_claim_and_forward_contract.rodtep_claim_and_forward_contract.doc_events.journal_entry.before_cancel",
        }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rodtep_claim_and_forward_contract.tasks.all"
# 	],
# 	"daily": [
# 		"rodtep_claim_and_forward_contract.tasks.daily"
# 	],
# 	"hourly": [
# 		"rodtep_claim_and_forward_contract.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rodtep_claim_and_forward_contract.tasks.weekly"
# 	],
# 	"monthly": [
# 		"rodtep_claim_and_forward_contract.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "rodtep_claim_and_forward_contract.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rodtep_claim_and_forward_contract.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rodtep_claim_and_forward_contract.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rodtep_claim_and_forward_contract.utils.before_request"]
# after_request = ["rodtep_claim_and_forward_contract.utils.after_request"]

# Job Events
# ----------
# before_job = ["rodtep_claim_and_forward_contract.utils.before_job"]
# after_job = ["rodtep_claim_and_forward_contract.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rodtep_claim_and_forward_contract.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
fixtures = [

    {
        "doctype": "Property Setter",
        "filters": [
            ["name", "in", ["Journal Entry-voucher_type-options"]]
        ],
    },
    {
         "dt": "Custom Field", 
         "filters":[["name", "in", ['Sales Order-amount_hedge','Bank-bank_type','Sales Order-natural_hedge','Payment Entry-forward_utilization','Payment Entry-forwards','Payment Entry-average_forward_rate','Payment Entry-total_amount_utilized']]]
      },
    
]


from . import __version__ as app_version

app_name = "snd_tinymce_editor"
app_title = "Snd Tinymce Editor"
app_publisher = "Sanad"
app_description = "Sanad tinymce Editor"
app_email = "alhakeem.prof@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/snd_tinymce_editor/css/snd_tinymce_editor.css"
# app_include_js = "/assets/snd_tinymce_editor/js/snd_tinymce_editor.js"
app_include_css = "/assets/snd_tinymce_editor/css/snd_tinymce_editor.css"
app_include_js = [
    # "https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.2.0/tinymce.min.js",
    "/assets/snd_tinymce_editor/tinymce/tinymce.js",
    "/assets/snd_tinymce_editor/js/snd_tinymce_editor.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/snd_tinymce_editor/css/snd_tinymce_editor.css"
# web_include_js = "/assets/snd_tinymce_editor/js/snd_tinymce_editor.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "snd_tinymce_editor/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "snd_tinymce_editor.utils.jinja_methods",
#	"filters": "snd_tinymce_editor.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "snd_tinymce_editor.install.before_install"
# after_install = "snd_tinymce_editor.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "snd_tinymce_editor.uninstall.before_uninstall"
# after_uninstall = "snd_tinymce_editor.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "snd_tinymce_editor.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"snd_tinymce_editor.tasks.all"
#	],
#	"daily": [
#		"snd_tinymce_editor.tasks.daily"
#	],
#	"hourly": [
#		"snd_tinymce_editor.tasks.hourly"
#	],
#	"weekly": [
#		"snd_tinymce_editor.tasks.weekly"
#	],
#	"monthly": [
#		"snd_tinymce_editor.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "snd_tinymce_editor.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "snd_tinymce_editor.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "snd_tinymce_editor.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"snd_tinymce_editor.auth.validate"
# ]

boot_session = "snd_tinymce_editor.startup.boot.boot_session"
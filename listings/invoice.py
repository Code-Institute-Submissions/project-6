from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from io import BytesIO
import xhtml2pdf.pisa as pisa
import os


class Invoice:

	def render_to_request(template_path, context_dict={}):
		template = get_template(template_path)
		html = template.render(context_dict)
		result = BytesIO()
		pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

		if not pdf.err:
			return HttpResponse(result.getvalue(), content_type='application/pdf')
		return None

	def render_to_file(path: str, params: dict):
		template = get_template(path)
		html = template.render(params)
		file_name = f"{str(params['file_name'])}.pdf"
		file_path = os.path.join(os.path.abspath(
			os.path.dirname("__file__")), "listings/invoices", file_name)	
		with open(file_path, 'wb') as pdf:
			pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
		return [file_name, file_path]

	def send_pdf(params):
		mail = EmailMultiAlternatives(
			subject=params['subject'],
			body=params['body'],
			from_email="The Key Keepers <admin@keykeppers.com>",
			to=params['to'],
			headers={"Reply-To": "support@keykeppers.com"}
		)
		mail.template_id = params['template_id']

		pdf = Invoice.render_to_file('invoice.html', params)

		with open(str(pdf[1]), 'rb') as file:
			mail.attachments = [
				(str(pdf[0]), file.read(), 'application/pdf')
			]

		try:
			mail.send()
		except Exception as e:
			print(e)

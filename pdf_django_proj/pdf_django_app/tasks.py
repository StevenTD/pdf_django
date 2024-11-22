import io
import time

from django.utils.timezone import localtime, now
from weasyprint import CSS, HTML
from django.core.files import File
from .models import PageRequest

def pdf(page):
    time.sleep(1)  # post_save fires after the save but before the transaction is committed

    if page.status != page.Status.PENDING:
        return

    page.status = PageRequest.Status.GENERATING
    page.save()

    try:
        html = HTML(url=page.url)
    except Exception as e:
        page.status = PageRequest.Status.ERROR
        page.error_msg = str(e)
        page.save()
        return

    try:
        # Create a timestamp using Django timezone in AM/PM format
        timestamp = localtime(now()).strftime('%Y-%m-%d %I:%M:%S %p')

        # Define CSS with page numbers and timestamp
        page_number_css = f"""
        @page {{
            @bottom-left {{
                content: "{timestamp}";
                font-size: 12px;
                color: gray;
            }}
            @bottom-center {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 12px;
                color: gray;
            }}
        }}
        """

        # Generate PDF with custom CSS
        pdf_in_memory = io.BytesIO()
        html.write_pdf(target=pdf_in_memory, stylesheets=[CSS(string=page_number_css)])
    except Exception as e:
        page.status = PageRequest.Status.ERROR
        page.error_msg = str(e)
        page.save()
        return

    page.pdf_file = File(pdf_in_memory, f"{page.pk}.pdf")
    page.status = PageRequest.Status.READY
    page.save()

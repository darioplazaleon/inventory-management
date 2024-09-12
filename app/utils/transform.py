import csv
import io
import json

from fpdf import FPDF
from fpdf.enums import TableCellFillMode
from starlette.responses import StreamingResponse

buffer = io.StringIO()


def export_products_to_csv(products, filename):
    writer = csv.writer(buffer)

    writer.writerow(["id", "name", "description", "price", "stock", "user_id"])

    for product in products:
        writer.writerow([product.id, product.name, product.description, product.price, product.stock, product.user_id])

    buffer.seek(0)

    response = StreamingResponse(buffer, media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response


def export_products_to_json(products, filename):
    products_dict = [product.__dict__ for product in products]
    for product in products_dict:
        product.pop('_sa_instance_state', None)  # Remove the internal state
    json.dump(products_dict, buffer)
    buffer.seek(0)

    response = StreamingResponse(buffer, media_type="application/json")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Product List', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_table(self, products):
        self.set_font('Arial', 'B', 12)
        self.cell(30, 10, 'ID', 1)
        self.cell(50, 10, 'Name', 1)
        self.cell(50, 10, 'Description', 1)
        self.cell(30, 10, 'Price', 1)
        self.cell(30, 10, 'Stock', 1)
        self.ln()

        self.set_font('Arial', '', 12)
        for product in products:
            self.cell(30, 10, str(product.id), 1)
            self.cell(50, 10, product.name, 1)
            self.cell(50, 10, product.description, 1)
            self.cell(30, 10, str(product.price), 1)
            self.cell(30, 10, str(product.stock), 1)
            self.ln()

def export_products_to_pdf(products, filename):
    pdf = PDF()
    pdf.add_page()
    pdf.add_table(products)
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    response = StreamingResponse(pdf_buffer, media_type="application/pdf")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

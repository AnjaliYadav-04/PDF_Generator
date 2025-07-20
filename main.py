from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, Frame, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import requests


# File path
pdf_file_path = "professional_weight_loss_program.pdf"

# Product details
product = {
    'name': 'Weight Loss 101',
    'description': 'A professionally designed 4-week program tailored to help beginners kickstart their weight loss journey. Includes a meal plan, daily workouts, and guidance from certified trainers.',
    'price': 599,
    'features': [
        ["Duration", "4 Weeks"],
        ["Trainer", "Dr. Fitwell"],
        ["Level", "Beginner"],
        ["Includes", "Meal Plan, Workout, Progress Tracker"]
    ],
    'image_path': "shopping_cart_icon.png"
}

#  icon
image_url = "https://cdn-icons-png.flaticon.com/512/1170/1170576.png"


try:
    img_data = requests.get(image_url).content
    with open(product['image_path'], 'wb') as handler:
        handler.write(img_data)
except:
    product['image_path'] = None

# Setup PDF
c = canvas.Canvas(pdf_file_path, pagesize=A4)
width, height = A4
styles = getSampleStyleSheet()
title_style = ParagraphStyle(name='Title', fontSize=22, leading=28, alignment=1, spaceAfter=20)
desc_style = ParagraphStyle(name='Desc', fontSize=12, leading=16)
label_style = ParagraphStyle(name='Label', fontSize=14, leading=18, textColor=colors.green, spaceAfter=10)

# Draw border box
margin = 50
c.setStrokeColor(colors.lightgrey)
c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

# Add image if available
if product['image_path']:
    c.drawImage(product['image_path'], width/2 - 0.75*inch, height - 180, width=1.5*inch, height=1.5*inch, preserveAspectRatio=True)

# Title
frame = Frame(margin + 20, height - 250, width - 2*margin - 40, 40, showBoundary=0)
frame.addFromList([Paragraph(f"<b>{product['name']}</b>", title_style)], c)

# Description
desc_frame = Frame(margin + 20, height - 330, width - 2*margin - 40, 70, showBoundary=0)
desc_frame.addFromList([Paragraph(product['description'], desc_style)], c)

# Price
price_frame = Frame(margin + 20, height - 370, width - 2*margin - 40, 30, showBoundary=0)
price_frame.addFromList([Paragraph(f"<b>Price:</b> ₹{product['price']}", label_style)], c)

# Features Table
data = [["Feature", "Detail"]] + product['features']
table = Table(data, colWidths=[2.2 * inch, 3.5 * inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.8, colors.grey),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke)
]))
table.wrapOn(c, width, height)
table.drawOn(c, margin + 20, height - 500)

# Footer
c.setFont("Helvetica-Oblique", 9)
c.setFillColor(colors.grey)
c.drawString(margin, margin - 10, "Generated as part of Digital Marketplace Project • Weight Loss PDF Module")

# Save
c.save()

pdf_file_path

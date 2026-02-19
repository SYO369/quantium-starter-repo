import csv
import glob
import os

def parse_price(p):
    if p is None:
        return 0.0
    p = p.strip()
    if p.startswith("$"):
        p = p[1:]
    p = p.replace(',', '')
    try:
        return float(p)
    except ValueError:
        return 0.0


def process(input_dir='data', output_file='formatted_sales_data.csv'):
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

    with open(output_file, 'w', newline='', encoding='utf-8') as out_f:
        writer = csv.writer(out_f)
        writer.writerow(['Sales', 'Date', 'Region'])

        for fn in sorted(csv_files):
            with open(fn, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = (row.get('product') or '').strip().lower()
                    if product != 'pink morsel':
                        continue

                    price = parse_price(row.get('price'))
                    qty_raw = (row.get('quantity') or '').strip()
                    try:
                        qty = int(qty_raw)
                    except Exception:
                        try:
                            qty = int(float(qty_raw))
                        except Exception:
                            qty = 0
                    sales = price * qty
                    date = (row.get('date') or '').strip()
                    region = (row.get('region') or '').strip()

                    writer.writerow([f"{sales:.2f}", date, region])


if __name__ == '__main__':
    process()

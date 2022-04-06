# import app.resources.model as rm
import csv
import sys
import uuid


def transform_resources(raw_csv_path, md_fldr_path):
    field_names = [
        'id',
        'title',
        'description',
        'content',
        'aspect',
        'goal',
        'sub_category',
        'image_name',
        'external_links']
    try:
        with open(raw_csv_path, 'r', encoding='utf-8-sig', newline='') as fr, open('data.csv', 'w+', encoding='utf-8', newline='') as fa:
            reader = csv.DictReader(f=fr, delimiter=',')
            writer = csv.DictWriter(f=fa, dialect='excel', fieldnames=field_names, delimiter=',')
            writer.writeheader()
            for row in reader:
                content = None
                md_path = row['File Path']
                if not (md_path is None or md_path == ""):
                    with open(md_fldr_path + '/' + md_path, 'r', encoding='utf-8-sig') as fmdr:
                        content = fmdr.read()
                        fmdr.close()
                writer.writerow({
                    'id': uuid.uuid4(),
                    'title': row["Name"],
                    'description': row['Description'],
                    'content': content,
                    'aspect': row['Aspect'],
                    'goal': row['Goal'],
                    'sub_category': row['Sub-categories'],
                    'image_name': row['Image Link'],
                    'external_links': row['External_Links']
                })
            fa.close()
            fr.close()
    except Exception as e:
        fr.close()
        fa.close()
        print("ERROR occurred while tansferring data from raw csv to db.")
        print(e)

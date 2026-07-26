# BS month names
bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
def convert_date(date_str, from_cal, to_cal):
    # Split the date
    year, month, day = map(int, date_str.split("-"))

    # Convert year
    if from_cal == to_cal:
        new_year = year
    elif from_cal == "AD" and to_cal == "BS":
        new_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        new_year = year - 56

    return new_year, month, day


def format_date(year, month, day, calendar, style):
    if style == "iso":
        return f"{year:04d}-{month:02d}-{day:02d} {calendar}"

    elif style == "full":
        if calendar == "BS":
            return f"{day}th {bs_months[month-1]}, {year} BS"
        else:
            return f"{day:02d}-{month:02d}-{year} AD"

    elif style == "nepali":
        if calendar == "BS":
            return f"{day} {bs_months[month-1]} {year} BS"
        else:
            return f"{day:02d}-{month:02d}-{year} AD"


# Process all customers
for customer in customers:
    year, month, day = convert_date(
        customer["date"],
        customer["cal"],
        customer["need"]
    )

    converted = format_date(
        year,
        month,
        day,
        customer["need"],
        customer["style"]
    )

    print(
        f'{customer["name"]} | Original: {customer["date"]} {customer["cal"]} | Converted: {converted}'
    )
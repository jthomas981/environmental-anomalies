import pathlib
import datetime
import csv

def get_data(start_date: datetime.date, end_date: datetime.date):
    """Start_data and end_data are formatted as YYYY-MM-DD"""
    events = ['earthquake', 'volcano', 'flood']
    environment_data = []
    for event in events:
        # Get environment data.
        path = pathlib.Path(f'backend/environment_data/{event}.csv')
        lines = path.read_text(encoding='utf-8').splitlines()
        environment_reader = csv.reader(lines)
        header_row = next(environment_reader)

        # Get column indexes from header row.
        start_year_index = header_row.index("Start Year")
        start_month_index = header_row.index("Start Month")
        start_day_index = header_row.index("Start Day")
        mag_index = header_row.index("Dis Mag Value")
        lat_index = header_row.index("Latitude")
        lon_index = header_row.index("Longitude")
        mag_scale_index = header_row.index("Dis Mag Scale")

        for row in environment_reader:
            # Check that a full date is present in data.
            start_day = row[start_day_index]
            start_month = row[start_month_index]
            start_year = row[start_year_index]
            if not start_day or not start_month or not start_year:
                continue

            row_date = datetime.date(int(row[start_year_index]),
                                    int(row[start_month_index]),
                                    int(start_day))
            magnitude = row[mag_index]

            if (start_date <= row_date <= end_date
                and magnitude):

                title = ""


                if magnitude:
                    title += f"{int(magnitude):,} {row[mag_scale_index]} "

                title += f"{event}"

                # Add location if recorded.
                location_index = header_row.index("Location")
                location = row[location_index]
                if location:
                    title += f" at {location}"

                # Add cost to title if there was any.
                cost_index = header_row.index("Reconstruction Costs ('000 US$)")
                cost = row[cost_index]
                if cost:
                    title += f" costing ${int(cost):,d}"

                title += "."
                title = title.capitalize()

                environment_entry = {
                    "Title": title,
                    "Date": row_date,
                    "Magnitude": magnitude,
                    "Latitude": row[lat_index],
                    "Longitude": row[lon_index],
                    "Event": event
                }  
                environment_data.append(environment_entry)

    return environment_data
"""Generate the Lesson 2 import practice files (fictional primary health centres).
Run:  python make_import_practice.py   (needs pandas, openpyxl, pyreadstat)
All records are fictional. The values are fixed, so everyone gets identical files."""
import csv, os
import pandas as pd

here = os.path.dirname(os.path.abspath(__file__))
rows = [
 # id,   name,                              state,    beds, staff, deliveries, pop,    rating, opened
 ("001", "Ajegunle PHC",                    "Lagos",  12, 18, 45,   123456, 3.5, "14/03/2015"),
 ("002", "St. Mary's, Ikeja",               "Lagos",  30, 41, 120,  210332, 4.2, "02/11/2009"),
 ("003", "Sabon Gari PHC",                  "Kano",    8, 11, 30,    98765, 2.8, "21/06/2018"),
 ("004", "Rafin Zurfi \"Model\" Clinic",    "Kaduna", 10, 14, None,  45210, 3.9, "05/01/2012"),
 ("005", "Bodija Health Centre",            "Oyo",    15, 22, 60,   156780, 4.0, "30/09/2010"),
 ("006", "Trans-Amadi PHC",                 "Rivers", 20, 27, 85,   187004, 3.2, "17/04/2014"),
 ("007", "Abakaliki Central, Ward 3",       "Ebonyi",  9, 12, 25,    67890, 3.0, "09/08/2016"),
 ("008", "Mushin Maternal Home",            "Lagos",  25, 33, 95,   175432, 4.5, "12/12/2008"),
 ("009", "Dala PHC",                        "Kano",   11, 15, 40,    88123, 3.1, "23/02/2017"),
 ("010", "Iyaganku Clinic",                 "Oyo",    14, 19, 52,   134500, 3.7, "01/07/2013"),
 ("011", "Port Harcourt Road PHC",          "Rivers", 18, 24, 70,   160250, 3.6, "28/05/2011"),
 ("012", "Zaria Road Health Post",          "Kaduna",  6,  8, 18,    39800, 2.5, "15/10/2019"),
]
cols = ["facility_id","facility name","state","beds","staff","monthly_deliveries","catchment_pop","rating","opened"]

def fmt(v, dec=".", na="NA"):
    if v is None: return na
    if isinstance(v, float): return str(v).replace(".", dec)
    return v

# 1. comma-delimited, header, quoted fields, NA text, UTF-8
with open(os.path.join(here, "phc_comma.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(cols)
    for r in rows: w.writerow([fmt(v) for v in r])

# 2. semicolon-delimited with decimal commas
with open(os.path.join(here, "phc_semicolon.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(cols)
    for r in rows: w.writerow([fmt(v, dec=",") for v in r])

# 3. tab-delimited
with open(os.path.join(here, "phc_tab.txt"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(cols)
    for r in rows: w.writerow([fmt(v) for v in r])

# 4. no header row
with open(os.path.join(here, "phc_noheader.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in rows: w.writerow([fmt(v) for v in r])

# 5. Latin-1 (ISO-8859-1) encoded file with accented characters
lat = [("001","Hôpital Général de Lomé","Lagos"),("002","Clínica São José","Kano"),("003","Zürich Mission Clinic","Oyo")]
with open(os.path.join(here, "phc_latin1.csv"), "w", newline="", encoding="latin-1") as f:
    w = csv.writer(f); w.writerow(["facility_id","facility_name","state"])
    for r in lat: w.writerow(r)

# 6. fixed-width text: id(1-3) name(4-33) state(34-41) beds(42-44) staff(45-47)
with open(os.path.join(here, "phc_fixed.txt"), "w", encoding="utf-8") as f:
    for r in rows:
        f.write(f"{r[0]:<3}{r[1][:30]:<30}{r[2]:<8}{r[3]:>3}{r[4]:>3}\n")

# 7. Excel workbook with three sheets
with pd.ExcelWriter(os.path.join(here, "phc_workbook.xlsx")) as xw:
    pd.DataFrame({"README": ["Fictional PHC data for the DATAQUEST course.",
                             "Sheet Q1_2025 has three title rows above the header.",
                             "Sheet Q2_2025 has the header in row 1."]}).to_excel(xw, sheet_name="README", index=False)
    q1 = pd.DataFrame(rows, columns=cols).iloc[:, :6]
    q1["monthly_deliveries"] = q1["monthly_deliveries"].astype("Int64")
    title = pd.DataFrame([["Primary health centre report, Q1 2025", None,None,None,None,None],
                          ["Prepared by: Planning Unit", None,None,None,None,None],
                          [None,None,None,None,None,None]])
    title.to_excel(xw, sheet_name="Q1_2025", index=False, header=False)
    q1.to_excel(xw, sheet_name="Q1_2025", index=False, startrow=3)
    q2 = pd.DataFrame(rows, columns=cols).iloc[:, :6].copy()
    q2["monthly_deliveries"] = (q2["monthly_deliveries"].fillna(0)*1.1).round().astype(int)
    q2.to_excel(xw, sheet_name="Q2_2025", index=False)

# 8. SPSS file with variable and value labels
import pyreadstat
df = pd.DataFrame(rows, columns=cols)
df["state_code"] = df["state"].map({"Lagos":1,"Kano":2,"Kaduna":3,"Oyo":4,"Rivers":5,"Ebonyi":6})
out = df[["facility_id","state_code","beds","staff","rating"]].copy()
out.columns = ["facility_id","state","beds","staff","rating"]
pyreadstat.write_sav(out, os.path.join(here, "phc_survey.sav"),
    column_labels=["Facility identifier","State","Number of beds","Number of staff","Patient rating (1-5)"],
    variable_value_labels={"state":{1:"Lagos",2:"Kano",3:"Kaduna",4:"Oyo",5:"Rivers",6:"Ebonyi"}})
print("files written to", here)

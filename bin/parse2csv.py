import os

TYPEFORM_API_KEY = os.environ.get("TYPEFORM_API_KEY", "")
assert TYPEFORM_API_KEY != "", "You need to call this script with your typeform api key in your environment variable: TYPEFORM_API_KEY"
print("TYPEFORM_API_KEY = ",TYPEFORM_API_KEY)

FORM_ID = os.environ.get("FORM_ID", "")
assert FORM_ID != "", "You need to call this script with your typeform id in your environment variable: FORM_ID"
print("FORM_ID = ",FORM_ID)

OUTPUT_CSV_PATH = os.environ.get("OUTPUT_CSV_PATH", "tf_out.csv")

from tfparser import parse_typeform_to_dataframe

if __name__ == "__main__":
    parse_typeform_to_dataframe(TYPEFORM_API_KEY, FORM_ID).to_csv(OUTPUT_CSV_PATH,index=False,encoding="utf8")
import typeform
import pandas as pd

def parse_typeform_to_dataframe(api_key, form_id, print_out_or_not=True):
    form = typeform.Form(api_key=api_key, form_id=form_id)


    # Fetch all responses to the form with default options
    responses = form.get_responses()
    data_list = []
    i = 0
    for response in responses:
        if len(response.answers) > 0:
            i += 1
            if print_out_or_not:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("i = ",i)
            data = {}
            for answer in response.answers:
                data[answer.question] = answer.answer
                if print_out_or_not:
                    print('{question}: {answer}'.format(question=answer.question, answer=answer.answer))
            data_list.append(data)
        
    df = pd.DataFrame(data_list)
    return df
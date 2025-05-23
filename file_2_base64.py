from base64 import b64decode, b64encode
import os

# Input file path
# file_path = r"C:\Users\suryavamsib\Desktop\AD-HOC\SutiTexTrak Testing Files Master\Testing_Status_Files\Exception\1696521482992_fxj6ci.pdf"


# with open( file_path, "rb") as pdf_file:
#     encoded_string = b64encode(pdf_file.read())

# # print(str(encoded_string)[2:-1])
# file_name = file_path.split('\\')[-1].split('.pdf')[0]

# out_file = fr'C:\Users\suryavamsib\Desktop\AD-HOC\Production_testing\{file_name}.txt'

# with open(out_file, 'wb') as sample_file:
#     sample_file.write(encoded_string)


main_path = r'F:\Delivery Note SutiProcure\Dataset'
try:
    for path, folders_list, files_list in os.walk(main_path):
        print('folders_list is: ', folders_list)
        print('files_list is: ', files_list)
        print('path is: ', path)
        print('-----------------------------------------------')
        if files_list:
            # pdf_list = [x for x in files_list if x.endswith('.pdf')]
            pdf_list = [x for x in files_list]

            if pdf_list:
                print('Found pdf files')
                for file in pdf_list:
                    file_path = os.path.join(main_path, path, file)
                    with open( file_path, "rb") as pdf_file:
                        encoded_string = b64encode(pdf_file.read())
                    base64_file_name = file_path.split('\\')[-1].split('.pdf')[0] + '.txt'
                    # base64_file_name = file_path.split('\\')[-1].rsplit('.')[0] + '.txt'
                    out_file_path = os.path.join(main_path, path, base64_file_name)

                    with open(out_file_path, 'wb') as sample_file:
                        sample_file.write(encoded_string)
except Exception as e:
    print(e)
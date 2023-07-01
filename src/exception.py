# anything want to work with exception
# can search exception python documentation
# or custom exception handling python

import sys 
#-> provide various function and variable that are used to manipulate python runtime environment


# create custom error message
def error_message_detail(error, error_detail:sys):

    _,_, exc_tb = error_detail.exc_info() # get execution info
    
    file_name =  exc_tb.tb_frame.f_code.co_filename # get the error file name


    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message



# test exception
# import logging
# if __name__== "__main__":

#     try:
#         a = 1/0

#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
    
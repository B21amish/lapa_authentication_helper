from lapa_authentication_helper.main import LAPAAuthenticationHelper

lapa_authentication_helper = LAPAAuthenticationHelper()

# Example: Register
email = "test@gmail.com"
password = "test@123"
registration_type = "email"
register_output = lapa_authentication_helper.register(email, password, registration_type)
print(register_output)

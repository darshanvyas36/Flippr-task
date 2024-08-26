from customer_service import CustomerService

if __name__ == "__main__":
    jdbc_url = "jdbc:mysql://localhost:3306/ecommerce"
    jdbc_user = "root"
    jdbc_password = "password"

    customer_service = CustomerService(jdbc_url, jdbc_user, jdbc_password)

    # Example usage
    sign_up_response = customer_service.sign_up("John Doe", "john.doe@example.com", "password123", "123 Main St")
    print(sign_up_response)

    sign_in_response = customer_service.sign_in("john.doe@example.com", "password123")
    print(sign_in_response)

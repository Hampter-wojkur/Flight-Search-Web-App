import smtplib
import os


class NotificationManager:

    sending_mail = "wojciechmarcela7@gmail.com"
    sending_password = os.environ.get('sending_password')

    def return_single_flight(self, flight_dict):
        
        if flight_dict:
            if flight_dict["stepover_city"] is None:
                stopover_info = ""
            else:
                stopover_info = "Flight has 1 stop over, via " + flight_dict["stepover_city"] + "-" + flight_dict["stepover_IATA"]
        
            return f'We found a flight for you! Only {flight_dict["lowest_price"]} {flight_dict["currency"]} to fly from {flight_dict["dep_city"]}-{flight_dict["dep_IATA"]} to {flight_dict["dest_city"]}-{flight_dict["dest_IATA"]}, from {flight_dict["dep_date"]} to {flight_dict["back_date"]}.\n {stopover_info}'
        else:
            return "Sorry we couldn't find any flights with this requirements. Please change your filters."
            

        

    def send_emails(self, flights_dict):

        # Download user e-mails from database
        # data_manager = DataManager()
        # users = data_manager.get_users()

        if flights_dict["stepover_city"] is None:
            stopover_info = ""
        else:
            stopover_info = "Flight has 1 stop over, via " + flights_dict["stepover_city"] + "-" + flights_dict["stepover_IATA"]
        
        #Define users
        for user in users["users"]:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.sending_mail,
                                 password=self.sending_password)
                connection.sendmail(from_addr=self.sending_mail, to_addrs=user["email"],
                                    msg=f'Low price alert! Only {flights_dict["lowest_price"]}€ to fly from {flights_dict["dep_city"]}-{flights_dict["dep_IATA"]} to {flights_dict["dest_city"]}-{flights_dict["dest_IATA"]}, from {flights_dict["dep_date"]} to {flights_dict["back_date"]}.\n {stopover_info}'.encode('utf-8'))


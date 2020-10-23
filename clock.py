# Kishan Vekaria
import datetime


class Clock:
    def __init__(self, hour=0, minute=0, second=0):  # If caller does not supply arguments,
        self.__hour = hour  # they’ll get the default values of 0.
        self.__minute = minute
        self.__second = second

    def __str__(self):  # This let's object instances be converted to strings: print(str(clock1))
        """
        This method overrides the version from the object class and is called when you print a Clock.
        Adds leading 0 to self.__hour, self.__minute, or self.__second if their values are not double digits.
        """
        double_digit_number = False
        formatted_hour = self.__hour
        formatted_minute = self.__minute
        formatted_second = self.__second
        if self.__hour < 10:
            formatted_hour = "0" + str(self.__hour)
            double_digit_number = True
        if self.__minute < 10:
            formatted_minute = "0" + str(self.__minute)
            double_digit_number = True
        if self.__second < 10:
            formatted_second = "0" + str(self.__second)
            double_digit_number = True
        if double_digit_number:
            return "{0}:{1}:{2}".format(formatted_hour, formatted_minute, formatted_second)
        else:
            return "{0}:{1}:{2}".format(self.__hour, self.__minute, self.__second)

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute

    def second(self):
        return self.__second

    def set_hour(self, new_hour):
        if isinstance(new_hour, int):
            if 0 <= new_hour <= 23:
                self.__hour = new_hour
            else:
                raise Exception("Sorry, no numbers below 0 or above 23.")
        else:
            raise TypeError("new_hour passed to set_hour was not an int")

    def set_minute(self, new_minute):
        if isinstance(new_minute, int):
            if 0 <= new_minute <= 59:
                self.__minute = new_minute
            else:
                raise Exception("Sorry, no numbers below 0 or above 59.")
        else:
            raise TypeError("new_minute passed to set_minute was not an int")

    def set_second(self, new_second):
        if isinstance(new_second, int):
            if 0 <= new_second <= 59:
                self.__second = new_second
            else:
                raise Exception("Sorry, no numbers below 0 or above 59")
        else:
            raise TypeError("new_second passed to set_second was not an int")

    def advance_hour(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            if amount_to_advance >= 0:
                self.__hour += amount_to_advance
                if self.__hour > 23:
                    self.__hour %= 24
            else:
                raise Exception("amount_to_advance passed to advance_hour was less than 0")
        else:
            raise TypeError("amount_to_advance passed to advance_hour was not an int")

    def advance_minute(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            if amount_to_advance >= 0:
                self.__minute += amount_to_advance
                if self.__minute > 59:
                    clock1.advance_hour(self.__minute // 60)
                    self.__minute %= 60
            else:
                raise Exception("amount_to_advance passed to advance_minute was less than 0")
        else:
            raise TypeError("amount_to_advance passed to advance_minute was not an int")

    def set_to_current_time(self):
        now = datetime.datetime.now()
        self.__hour = int(now.strftime("%H"))
        self.__minute = int(now.strftime("%M"))
        self.__second = int(now.strftime("%S"))

    def __eq__(self, other):
        """
        This method overrides the version from the object class and lets you use == to compare Clocks
        """
        if isinstance(other, Clock):
            return self.__hour == other.__hour and self.__minute == other.__minute and self.__second == other.__second
        return False

    def __lt__(self, other):
        """
        This method lets you compare two clocks for order -- if the Clock object on the left
        hand side of the < is smaller, then __lt__ returns true
        """
        if isinstance(other, Clock):
            if self.__hour < other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute < other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second < other.__second:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Clock: " % other)

    def __gt__(self, other):
        if isinstance(other, Clock):
            if self.__hour > other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute > other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute > other.__minute and self.__second > other.__minute:
                return True
            else:
                return False

        raise Exception("other argument to greater than was not a Clock: " % other)

    # """
    # The below code was my attempt at __lt__ and __gt__ methods. Too many nested if/elif statements.
    # """
    # def __lt__(self, other):
    #     if self.__hour < other.__hour:
    #         return "The time is earlier"
    #     elif self.__hour == other.__hour:
    #         if self.__minute < other.__minute:
    #             return "The time is earlier"
    #         elif self.__minute == other.__minute:
    #             if self.__second < other.__second:
    #                 return "The time is earlier"
    #             else:
    #                 return "The time is not earlier"
    #     else:
    #         return "The time is not earlier"

    # def __gt__(self, other):
    #     if self.__hour > other.__hour:
    #         return "The time is later"
    #     elif self.__hour == other.__hour:
    #         if self.__minute > other.__minute:
    #             return "The time is later"
    #         elif self.__minute == other.__minute:
    #             if self.__second > other.__second:
    #                 return "The time is later"
    #             else:
    #                 return "The time is not later"
    #     else:
    #         return "The time is not later"


# clock1 = Clock()
# clock2 = Clock(22, 2, 3)
# print(clock1.__dict__)
# clock1.hour = 0
# clock1.minute = 0
# print(clock1.hour)
# print(clock1.minute)
# print(clock1.second)
# print(clock1.hour)
# print(str(clock1))
# clock1.set_minute(0)
# clock1.set_hour(0)
# print(clock1.__dict__)
# clock1.advance_hour(0)
# print(clock1.__dict__)
#
# clock1.set_to_current_time()
# print(clock1.__dict__)
# clock1.advance_minute(30)
clock1 = Clock(0, 0, 0)
clock2 = Clock(1, 1, 1)
print(clock1.__dict__)
print(clock2.__dict__)
# print(clock1.__lt__(clock2))
# print(clock1.__gt__(clock2))
# print(clock2.__lt__(clock1))
# print(clock2.__gt__(clock1))
# print(clock1.__lt__(clock1))
# print(clock1.__gt__(clock1))

print(clock1.__eq__(clock2))
clock1.advance_hour(24)
clock1.advance_minute(61)
print(clock1)
clock1.set_to_current_time()
print(clock1)


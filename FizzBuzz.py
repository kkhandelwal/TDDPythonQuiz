"""
Q1. Why is the report method untestable ? [2 pts]

report_file takes pointer of file , available on local machine- external collaborators


Q2. How will you change the api of the report method to make it more testable ? [2 pts]

Passing a Filehandlewrapper to report function , so that function should not pick his collaborators.
We can use -
a. Filehandlewrapper - a wrapper class defined to have interface function for OPen
b. fileopener = using argument in report function, Implemented below

"""
class FizzBuzz(object):
    def report(self, numbers,fileopener=open):

        #report_file = Filehandlewrapper.open
        report_file = fileopener('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))

            

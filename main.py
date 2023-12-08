# # from dtsc5502 import hello_dtsc5502 as ht
# import dtsc5502 as dtsc
# def main():
#   dtsc.hello_dtsc5502()



# if __name__ == '__main__':
#   main()
#   lst=[1,2,3,4,5,6,7,8,2]
#   print(dtsc.greeting("DTSC5502"))
#   print(dtsc.calculate_mean(lst))
#   print(dtsc.calculate_median(lst))
#   print(dtsc.calculate_mode(lst))

from dtsc5502.version import __version__
import dtsc5502.statistics as stats
# import stats.descriptive as de
import dtsc5502.probabilities.functions as pb

print(__version__)
lst=[1,2,3]
print(stats.descriptive.calculate_mean(lst))
# print(de.calculate_mean(lst))
print(pb.factorial(5))



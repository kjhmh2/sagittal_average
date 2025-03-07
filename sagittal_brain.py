from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np

def run_averages(file_input='brain_sample2.csv', file_output='brain_average2.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is the average for each sagittal/horizontal plane (rows)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    # correct bug
    averages = planes.mean(axis=1)[np.newaxis, :]

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')


if __name__ == "__main__":
    parser = ArgumentParser(description="Calculates the average for each sagittal-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="brain_sample2.csv",
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default="brain_average2.csv",
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)

# data_input = np.zeros((20, 20))
# data_input[-1, :] = 1
# np.savetxt("brain_sample2.csv", data_input, fmt='%d', delimiter=',')

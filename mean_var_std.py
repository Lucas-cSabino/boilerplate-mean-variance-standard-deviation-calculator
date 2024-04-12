import numpy as np



def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

#converting the list into a matrix    
    matriz = np.array(list).reshape(3,3)

#calculating the mean of both axes and the flattened matrix
    mean_0_axis = np.mean(matriz, axis=0).tolist()
    mean_1_axis = np.mean(matriz, axis=1).tolist()
    mean_flattened_matrix = np.mean(matriz)

#calculating the variance of both axes and the flattned matrix
    var_0_axis = np.var(matriz, axis=0).tolist()
    var_1_axis = np.var(matriz, axis=1).tolist()
    var_flattened_matrix = np.var(matriz)

#calculating the standard deviation of both axes and the flattned matrix

    std_0_axis = np.std(matriz, axis=0).tolist()
    std_1_axis = np.std(matriz, axis=1).tolist()
    std_flattened_matriz = np.std(matriz)

#calculating the max of both axes and the flattned matrix

    max_0_axis = np.max(matriz, axis=0).tolist()
    max_1_axis = np.max(matriz, axis=1).tolist()
    max_flattened_matrix = np.max(matriz)

#calculating the min of both axes and the flattned matrix

    min_0_axis = np.min(matriz, axis=0).tolist()
    min_1_axis = np.min(matriz, axis=1).tolist()
    min_flattened_matrix = np.min(matriz)

#calculating the sum of both axes and the flattned matrix

    sum_0_axis = np.sum(matriz, axis=0).tolist()
    sum_1_axis = np.sum(matriz, axis=1).tolist()
    sum_flattened_matrix = np.sum(matriz)



    calculations = {
        'mean': [mean_0_axis, mean_1_axis, mean_flattened_matrix],
        'variance': [var_0_axis, var_1_axis, var_flattened_matrix],
        'standard deviation': [std_0_axis, std_1_axis, std_flattened_matriz],
        'max': [max_0_axis, max_1_axis, max_flattened_matrix],
        'min': [min_0_axis, min_1_axis, min_flattened_matrix],
        'sum': [sum_0_axis, sum_1_axis, sum_flattened_matrix],
    }

    
    return calculations


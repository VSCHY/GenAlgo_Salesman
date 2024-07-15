import numpy as np
import matplotlib.pyplot as plt


def plot_outcomes(D, name_indicator):
    out = np.zeros((21,10))

    fig = plt.figure(figsize = (8,5))
    for n, option in enumerate(D.keys()):
        for i, k in enumerate(D[option]):
            data = np.array(k[name_indicator])
            data_out = np.copy(data)

            for j in range(1,21):
                data_out[j] = np.min(data[:j])
            out[:,i] = data_out


        d_mean = np.mean(out, axis =1)/1000
        d_max = np.max(out, axis =1)/1000
        d_min = np.min(out, axis =1)/1000

        x = np.arange(21)
        ax = fig.add_subplot(2,3,n+1)
        ax.fill_between(x, d_min, d_max, alpha = 0.5)
        ax.plot(x, d_mean)
        if name_indicator == "best_fitness":
            plt.ylim(8,25)
        elif name_indicator == "average_fitness":
            plt.ylim(8,40)
        elif name_indicator == "fitness_variance":
            plt.ylim(2,4)
        
        plt.title(option)
    plt.suptitle(name_indicator.replace("_"," ").title())
    fig.subplots_adjust(top = 0.9, bottom = 0.05, left = 0.05, right = 0.98, wspace= 0.2, hspace=0.3)

    return fig
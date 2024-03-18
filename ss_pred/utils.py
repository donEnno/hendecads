import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_prediction(y_pred, y_test,
                    save_fig=False, fig_path=None):
    p1 = np.argmax(y_pred, axis=-1)[0]
    y1 = np.argmax(y_test, axis=-1)[0]
    
    c = np.array([p1, y1])

    _, ax = plt.subplots(figsize=(16, 1))

    sns.heatmap(c, ax=ax, cmap='viridis', xticklabels=[], cbar=False)
    ax.set_yticklabels(['Predicted', 'True'], rotation=0)
    
    labels = ['P', 'C', 'X']
    colors = ['#440154', '#21918c', '#fde725']
    patches = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
    ax.legend(patches, labels, loc='center left', bbox_to_anchor=(1, 0.5))
    
    if save_fig:
        plt.savefig(fig_path, bbox_inches='tight')
    else:
        plt.show()


def plot_confusion_matrix(i, y_pred, y_test,
                          save_fig=False, fig_path=None):
    p1 = np.argmax(y_pred, axis=-1)[0]
    y1 = np.argmax(y_test, axis=-1)[0]
    
    p1 = p1[y1 > 0]
    y1 = y1[y1 > 0]

    c = np.zeros((2, 2), dtype=int)
    for i in range(1, 3):
        for j in range(1, 3):
            c[i-1, j-1] = int(np.sum((p1 == i) & (y1 == j)))
        
    _, ax = plt.subplots(figsize=(4, 4))
    sns.heatmap(c, annot=True, fmt='d', linewidths=0.55, linecolor='black', cbar=False)
    
    ax.set_ylabel('Predicted')
    ax.set_xlabel('True')

    ax.set_xticklabels(['C', 'X'])
    ax.set_yticklabels(['C', 'X'], rotation=0)

    if save_fig:
        plt.savefig(fig_path, bbox_inches='tight')
    else:
        plt.show()
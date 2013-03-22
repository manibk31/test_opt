from pygmin.potentials import BasePotential

class BaseFunction(BasePotential):
    pass

    def f(self, x):
        return self.getEnergy(x)
    
    def fg(self, x):
        return self.getEnergyGradient(x)


def makeplot2d(f, nx=100):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    import matplotlib.pyplot as plt
    import numpy as np
    
    ny = nx
    xmin, ymin = f.xmin[:2]
    xmax, ymax = f.xmax[:2]
    x = np.arange(xmin, xmax, (xmax-xmin)/nx)
    y = np.arange(ymin, ymax, (ymax-ymin)/ny)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    for i in range(x.size):
        for j in range(y.size):
            xy = np.array([X[i,j], Y[i,j]])
            Z[i,j] = f.getEnergy(xy)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
    
#    ax.set_zlim(-1.01, 1.01)

#    ax.zaxis.set_major_locator(LinearLocator(10))
#    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.show()
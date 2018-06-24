
get_ipython().run_line_magic('matplotlib', 'inline')


# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

#2D Plot
fig=plt.figure()
ax=fig.add_subplot(111)
#it doesn't matter if I add a comma between the 111. Either way it works.
plt.scatter(x,y, c='purple', marker='*')


#3D plot

fig_3d=plt.figure()
ax=fig_3d.add_subplot(111, projection="3d")

constellation3d=ax.scatter(x,y,z, c='r', marker='*')
ax.set_title("Orion Constellation")
ax.set_xlabel("X axis", size=6.5)
ax.set_ylabel("Y axis", size=6.5)
ax.set_zlabel("Z axis", size=6.5)


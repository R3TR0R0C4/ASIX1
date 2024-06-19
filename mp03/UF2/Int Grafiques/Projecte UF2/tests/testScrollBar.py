"""from tkinter import *

window = Tk() #generem finestra
window.geometry("300x300") #declarem la mida de finestra
window.configure(bg="light Grey") #configurem color de fons
window.title("") #configurem nom de finestra
window.resizable(False, False) #configurem que no es pugui canviar la mida de la finestra

scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill=Y )

labelTest1=Label(
    text="Test label"
)
labelTest1.pack()

labelTest2=Label(
    text="Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit.\n Ut viverra vestibulum tortor,\n vel porta arcu fermentum nec\n. Mauris vel lectus eu\n erat finibus malesuada vitae aliquam\n sapien. Curabitur ornare\n posuere congue. Pellentesque at\n augue libero. Nunc\n id nisl et dui\n blandit accumsan. Cras\n dignissim neque sed quam\n pulvinar, aliquet egestas\n mi\n sagittis. Proin vel dapibus\n ex. Quisque cursus\n elit ac nisi\n efficitur, at vestibulum\n est feugiat.\n Orci varius natoque penatibus\n et magnis dis\n parturient montes, nascetur\n ridiculus mus. Maecenas\n vitae ligula non ex tincidunt\n pretium. Nam sodales\n ultricies tempor. Vestibulum\n elementum nec lectus sit\n amet malesuada.\n Nam a eros\n rutrum, tincidunt mauris\n sit amet, lacinia justo. Aenean in nulla vitae est luctus gravida. Ut lacus lacus, hendrerit nec ultricies non, scelerisque a tellus. Suspendisse malesuada porta velit, id sodales dui vehicula eget. Duis leo turpis, blandit at tellus vitae, ullamcorper mattis risus. Fusce in nisl tristique, pharetra dui ac, hendrerit turpis. Ut ullamcorper odio non malesuada aliquam. In pharetra urna finibus, interdum lorem vel, varius lorem. Mauris dictum maximus erat, et tincidunt purus finibus aliquet. Donec pretium mattis ligula, ac feugiat turpis interdum et. Vivamus posuere nisi eleifend elit suscipit imperdiet. Duis sodales mauris mauris, ac faucibus dui vestibulum nec. Curabitur eleifend pulvinar risus sed vulputate. Quisque id dolor et magna fermentum rhoncus. Vestibulum risus nunc, rhoncus efficitur est ut, ultricies porttitor nibh. Praesent at massa eget felis pellentesque maximus nec eu ipsum. Donec lacinia blandit euismod. Vestibulum interdum rutrum enim, vel suscipit urna volutpat vitae. Nam quis metus at est finibus condimentum quis ac metus. Nam eu magna eu mi pharetra hendrerit at nec ipsum. Pellentesque aliquet aliquet elit in vestibulum. Vestibulum ultricies, nisi sit amet iaculis mollis, ligula nunc facilisis leo, in mollis metus lacus id felis. Mauris eu nunc sodales massa cursus euismod. Nulla quis tellus neque. Nullam vel magna vehicula, lobortis tortor sed, tincidunt mauris. Morbi in finibus ligula, id volutpat risus. Duis consequat nisi et metus vulputate, ut euismod mi sollicitudin. Integer pulvinar, leo sit amet consequat ultrices, urna erat laoreet orci, a scelerisque risus dolor id lectus. Integer quis venenatis turpis. In accumsan luctus ipsum id sollicitudin. Sed consequat lacinia sapien, quis malesuada elit pharetra sed. Ut blandit interdum ex. Quisque maximus condimentum placerat. Nullam sed eros a sapien ullamcorper varius. Ut non nibh iaculis, cursus eros sit amet, luctus metus. Donec tempor tristique condimentum. Etiam rutrum elit eu purus tincidunt, ut dapibus nulla lacinia. Aenean non orci nulla. Donec dictum nisi ante, quis feugiat neque imperdiet et. In tempus nibh non metus fringilla, quis gravida libero imperdiet. Suspendisse bibendum risus vitae massa tempus condimentum. Nulla ante magna, egestas sed congue vel, tempor a ex. Cras urna mauris, accumsan ac urna quis, venenatis tincidunt sem. Suspendisse sit amet ipsum leo. Sed a lectus lorem. Donec porta placerat dui nec luctus. Mauris hendrerit, elit eu venenatis aliquam, urna eros vulputate dolor, pharetra blandit mauris mauris eget enim."
)
labelTest2.pack()

scrollbar.config( command = labelTest1 )

window.mainloop()"""

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))
   
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
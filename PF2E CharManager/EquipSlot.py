from Entity import *
import Functions as Foo
from Variables import yesNo


class EquipSlot(Entity):

    def __init__(self, *args):

        Entity.__init__(self, * args)
        self.item = None
        self.isFull = False

    def equip(self, item):  # p2TODO: auto adjust armor bulk
        if not self.isFull:
            self.item = item
            self.isFull = True
        elif self.isFull:
            pick = Foo.getChoice(yesNo, "Should " + self.item.name + " be replaced with " + item.name + "?")
            if pick == "Yes":
                self.item = item

    def unEquip(self):
        if self.isFull:
            self.item = None
            self.isFull = False


slot = EquipSlot("", "")

slotRIGHTHAND = EquipSlot("Right Hand", "Slot for holding items in right hand")
slotLEFTHAND = EquipSlot("Left Hand", "Slot for holding items in right hand")
slotARMOR = EquipSlot("Armor", "Slot for worn body armor")

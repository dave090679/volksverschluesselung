#appModules/volksverschluesselung.py#A part of NonVisual Desktop Access (NVDA)#Copyright (C) 2006-2012 NVDA Contributors#This file is covered by the GNU General Public License.#See the file COPYING for more details.import appModuleHandlerimport apiimport controlTypesfrom NVDAObjects.UIA import UIAclass vvlistitem(UIA):	def _get_name(self):		l = list()		for x in self.children:			childname = x.name			childrole = x.role			if childrole == controlTypes.ROLE_STATICTEXT:				l.append(childname)		return '; '.join(l)class  vvunlabeledbutton(UIA):
	def _get_name(self):
		uianame = self.UIAElement.CurrentName		if uianame != '':			s = uianame		else:			l = list()			for x in self.children:				childname = x.name				if childname != '':					l.append(childname)			try:				s = l[0]			except:				s = ''		return s
	def _get_description(self):
		uiadesc = self.UIAElement.CurrentHelpText		if uiadesc != '':			s = uiadesc		else:			l = list()			for x in self.children:				childname = x.name				if childname != '':					l.append(childname)			try:				s = l[1]			except:				s = ''		return s

class AppModule(appModuleHandler.AppModule):	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if isinstance(obj, UIA):			if obj.role == controlTypes.ROLE_BUTTON:
				clslist.insert(0,vvunlabeledbutton)
			elif obj.role == controlTypes.ROLE_LISTITEM:					clslist.insert(0, vvlistitem)
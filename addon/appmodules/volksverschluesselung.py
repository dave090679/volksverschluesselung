#appModules/volksverschluesselung.py
	def _get_name(self):
		uianame = self.UIAElement.CurrentName
	def _get_description(self):
		uiadesc = self.UIAElement.CurrentHelpText

class AppModule(appModuleHandler.AppModule):
		if isinstance(obj, UIA):
				clslist.insert(0,vvunlabeledbutton)
			elif obj.role == controlTypes.ROLE_LISTITEM:
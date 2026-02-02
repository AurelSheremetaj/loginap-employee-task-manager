from enums import UserFeatures,UserRole
from admin_view import EmployeeManagerContentPanel,TaskManagerContentPanel


class AuthorizationService:
    def get_feature_user_by_user_role(self,user_role):
        if user_role == UserRole.ADMIN:
            return [UserFeatures.EMPLOYEES,
                    UserFeatures.DEPARTMENTS,
                    UserFeatures.TASK,
                    UserFeatures.PAYROLLS,
                    UserFeatures.ACCOUNTS,
                    UserFeatures.HOLIDAYS,
                    UserFeatures.SIGN_OUT]
            
        elif user_role == UserRole.EMPLOYEE:
            return [UserFeatures.CUSTOMERS,
                    UserFeatures.TASK,
                    UserFeatures.SALES,
                    UserFeatures.CALENDAR,
                    UserFeatures.SIGN_OUT]
            
        elif user_role == UserRole.INTERN:
            return [UserFeatures.CALENDAR,
                    UserFeatures.TASK,
                    UserFeatures.SIGN_OUT]
            
        elif user_role is None:
            raise RuntimeError ("The provided user role" + user_role + "is not supported")
        
        
class UserFeatureLabelResolever:
    user_feature_label_dict = None
    
    @staticmethod
    def get_user_feature_label(user_feature):
        return UserFeatureLabelResolever.__get_user_feature_label_dict().get(user_feature)
        
        
        
    @staticmethod
    def __get_user_feature_label_dict():
        if UserFeatureLabelResolever.user_feature_label_dict is None:
            UserFeatureLabelResolever.user_feature_label_dict = {
                UserFeatures.EMPLOYEES: "Employees",
                UserFeatures.DEPARTMENTS:  "Departments",
                UserFeatures.PAYROLLS:  "Payrolls",
                UserFeatures.HOLIDAYS:  "Holidays",
                UserFeatures.ACCOUNTS: "Accounts",
                UserFeatures.CUSTOMERS: "Customers",
                UserFeatures.SALES: "Sales",
                UserFeatures.CALENDAR: "Calendar",
                UserFeatures.TASK:"Task",
                UserFeatures.SIGN_OUT:"Sign Out"
                
            }
        return UserFeatureLabelResolever.user_feature_label_dict
        
        
class UserFeatureContentPanelResolver:
    user_feature_content_panel_map = None
    
    @staticmethod 
    def get_user_feature_panel(user_feature):
        return UserFeatureContentPanelResolver.get_user_feature_content_panel_map().get(user_feature)
    
    
    @staticmethod
    def get_user_feature_content_panel_map():
        if UserFeatureContentPanelResolver.user_feature_content_panel_map is None:
            UserFeatureContentPanelResolver.user_feature_content_panel_map = {
                "Employees" : EmployeeManagerContentPanel(),
                "Task" : TaskManagerContentPanel(),
            }
        return UserFeatureContentPanelResolver.user_feature_content_panel_map
    
    
    

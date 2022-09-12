# Flask Blog Project

-----------

基于Python Flask框架实现的简单Blog项目

**User**

1. 注册（register）
   - `flask_wtf.FlaskForm`作为父类实现注册表单
   - `flask-sqlalchemy`实现数据库交互（用户数据验证）
   - `flask_bcrypt`实现数据加密处理
   - `flask_login`实现登录逻辑
   - `flask`提供跳转、获取模板、重定向、页面提示信息、URL参数获取等功能
2. 登录（login）
   - `flask_bcrypt`实现密码校验
3. 重置密码（reset_password）
   - `python-jose.jwt`实现`token`生成与校验
   - `flask_mail`的`Message`组装邮件体与发件信息、`Mail`发送邮件请求
4. 设置账户（account）
   - `Pillow`中的`Image`实现对图像大小的统一处理及保存
   - `secrets`提供hex字符串，拼接图片文件名
   - `os`获取图片文件扩展名，拼接出当前项目中图片的存储路径
5. 登出（logout）
   - `flask_login`的`logout_user`实现

**Post**

1. 新增（new）/ 修改（update）/ 删除（delete）
   - `flask-sqlalchemy`
   - `flask_wtf.FlaskForm`

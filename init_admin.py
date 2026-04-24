"""
初始化管理员账号脚本
运行: python init_admin.py
"""
import hashlib
import sqlite3
import getpass

def create_admin():
    username = input("输入管理员用户名 [admin]: ").strip() or "admin"
    password = getpass.getpass("输入管理员密码: ")
    confirm = getpass.getpass("确认密码: ")
    
    if password != confirm:
        print("❌ 两次密码不一致")
        return
    
    if len(password) < 6:
        print("❌ 密码长度至少6位")
        return
    
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect("api_relay.db")
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO admins (username, password_hash) VALUES (?, ?)",
                  (username, hashed))
        conn.commit()
        print(f"✅ 管理员 '{username}' 创建成功")
    except sqlite3.IntegrityError:
        print(f"❌ 用户名 '{username}' 已存在")
    finally:
        conn.close()

if __name__ == "__main__":
    create_admin()

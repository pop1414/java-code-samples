package com.spike.entity;

import java.io.Serial;
import java.io.Serializable;
import java.sql.Timestamp;

import lombok.Data;

@Data
public class User implements Serializable {
    private Long id;

    private String userName;

    private String password;

    private String email;

    private Timestamp createTime; // 创建时间（数据库自动填充）

    private Timestamp updateTime; // 更新时间（数据库自动填充）

    @Serial
    private static final long serialVersionUID = 1L;

    // 无参构造（MyBatis必须）
    public User() {
    }

    // 插入用户时的构造器（无需id、时间字段）
    public User(String userName, String password, String email) {
        this.userName = userName;
        this.password = password;
        this.email = email;
    }
}

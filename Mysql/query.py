class Query:

    #database
    drop_database = 'drop database if exists management;'
    create_database = 'Create database management;'
    use_database = 'use management;'

    #tables
    create_table_item = """
    Create table item (
        icode Int Auto_Increment Primary Key,
        iname Varchar(50) Not Null,
        icategory varchar(20) Not Null,
        idesc varchar(100) Not Null,
        mrp float Not Null
    );
    """
    create_table_inv = """
    create table inventory (
        icode int AUTO_INCREMENT PRIMARY KEY,
        stock int default 0,
        foreign Key(icode) references item(icode)
    );
    """
    create_table_customer = """
    Create table customer (
        ccode int AUTO_INCREMENT primary key,
        cname varchar(30) Not Null,
        address varchar(50) Not Null,
        phoneno bigint unique,
        email varchar(20) Not Null unique,
        first_p timestamp Not null
    );
    """
    create_table_sales = """
    Create table sales (
        scode int AUTO_INCREMENT primary key,
        icode int,
        ccode int,
        price float not null, 
        s_date timestamp unique,
        foreign key (icode) references item(icode),
        foreign key (code) references customer(ccode)
    );
    """
    create_table_advances = """
    Create table advances (
        ccode int primary key,
        loan float,
        ad_date timestamp Not null,
        foreign key (ccode) references customer(ccode)
    );
    """

    #Alter tables
    alter_table_item = 'Alter Table item Engine = innodb;'
    alter_table_inv = 'Alter Table inventory Engine = innodb;'
    alter_table_customer = 'Alter Table customer Engine = innodb;'
    alter_table_sales = 'Alter Table sales Engine = innodb;'
    alter_table_advances = 'Alter Table advances Engine = innodb;'

    setup_queries = [
        drop_database,
        create_database,
        use_database,
        create_table_item,
        create_table_inv,
        create_table_customer,
        create_table_sales,
        create_table_advances,
        alter_table_item,
        alter_table_inv,
        alter_table_customer,
        alter_table_sales,
        alter_table_advances
    ]

    tables = [
        'item',
        'inventory',
        'customer',
        'sales',
        'advances'
    ]

    def table_attributes(self, table):
        if table == 'item':
            return ['icode', 'iname', 'icategory', 'idesc', 'mrp']
        
        elif table == 'inventory':
            return ['icode', 'stock']
        
        elif table == 'customer':
            return ['ccode', 'cname', 'address', 'phoneno', 'email', 'first_p']

        elif table == 'sales':
            return ['scode', 'icode', 'ccode', 'price', 's_date']

        elif table == 'advances':
            return ['ccode', 'loan', 'ad_date']

        else:
            return False

    def insert(self, table):
        if table == 'item':
            return """
            Insert into item (iname, icategory, idesc, mrp)
            values (%s, %s, %s, %s);
            """

        elif table == 'inventory':
            return """
            Insert into inventory (icode, stock)
            values (%s, %s);
            """

        elif table == 'customer':
            return """
            Insert into customer (cname, address, phoneno, email, first_p)
            values (%s, %s, %s, %s, sys());
            """

        elif table == 'sales':
            return """
            Insert into sales (icode, ccode, price, s_date)
            values (%s, %s, %s, sys());
            """
        
        elif table == 'advances':
            return """
            Insert into advances (ccode, load, ad_date)
            values (%s, %s, sys());
            """
        
        else:
            return False

    def update(self, table):
        if table == 'item':
            return """
            Update item
            Set iname = %s, icategory = %s, idesc = %s, mrp = %s
            Where icode = %s;
            """
        
        elif table == "inventory":
            return """
            Update inventory
            Set stock = %s
            where icode = %s; 
            """

        elif table == 'customer':
            return """
            Update customer
            Set cname = %s, address = %s, phoneno = %s, email = %s
            where ccode = %s;
            """

        elif table == 'sales':
            return """
            Update Sales
            Set icode = %s, ccode = %s, price = %s
            where scode = %s;
            """
        
        elif table == 'advances':
            return """
            Update advances
            Set loan = %s
            where ccode = %s;
            """

        else:
            return False
    
    def delete(self, table):
        if table == 'item':
            return """
            Delete from item 
            where icode = %s;
            """
        
        elif table == 'inventory':
            return """
            Delete from inventory
            where icode = %s;
            """

        elif table == 'customer':
            return """
            Delete from customer
            where ccode = %s;
            """

        elif table == 'sales':
            return """
            Delete from sales
            where scode = %s;
            """

        elif table == 'advances':
            return """
            Delete from advances
            where ccode = %s;
            """

        else:
            return False

    def select(self, table):
        if table == 'item':
            return 'Select  * from item;'
        
        elif table == 'inventory':
            return 'Select * from inventory;'
        
        elif table == 'customer':
            return 'Select * from customer;'

        elif table == 'sales':
            return 'Select * from sales;'

        elif table == 'advances':
            return 'Select * from advances;'

        else:
            return False

    def select_where(self, table):
        if table == 'item':
            return """
            Select  * from item
            Where %s = %s;
            """
        
        elif table == 'inventory':
            return """
            Select * from inventory
            where %s = %s;
            """
        
        elif table == 'customer':
            return """
            Select * from customer
            where %s = %s;
            """

        elif table == 'sales':
            return """
            Select * from sales
            where %s = %s;
            """

        elif table == 'advances':
            return """
            Select * from advances
            where %s = %s;
            """

        else:
            return False
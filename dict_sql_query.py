'''
    This module contains SQL queries.
    Queries are direct copy of what's in ../SQL folder.
'''

qry_provider = '''
    /* IICT */
    SELECT DISTINCT 
        pm.FIRSTNAME, 
        pm.LASTNAME, 
        pm.MI, 
        pm.FULLNAME, 
        pm.REV_FULLNAME, 
        pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
        pm.FROMDATE, 
        pm.TERMDATE, 
        ps.SPECCODE, 
        ps.SPECDESCR, 
        pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
        vm.VENDORNM, 
        pv.THRUDATE, 
        vm.VENDORNM1, 
        vm.VENDORNM2, 
        pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
        pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
        pa.EXPDATE, 
        pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
    FROM IICT.dbo.VEND_MASTERS_V vm
        INNER JOIN IICT.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
        INNER JOIN IICT.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
        LEFT OUTER JOIN IICT.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
        RIGHT OUTER JOIN IICT.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
        LEFT OUTER JOIN IICT.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
    WHERE        
        pm.CONTRACT IN ('1', '2', '6', '7')
        AND pa.EXPDATE IS NULL
        AND pm.TERMDATE IS NULL

    /* IMPERIAL */
    UNION ALL
    SELECT DISTINCT 
        pm.FIRSTNAME, 
        pm.LASTNAME, 
        pm.MI, 
        pm.FULLNAME, 
        pm.REV_FULLNAME, 
        pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
        pm.FROMDATE, 
        pm.TERMDATE, 
        ps.SPECCODE, 
        ps.SPECDESCR, 
        pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
        vm.VENDORNM, 
        pv.THRUDATE, 
        vm.VENDORNM1, 
        vm.VENDORNM2, 
        pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
        pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
        pa.EXPDATE, 
        pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
    FROM IMPERIAL.dbo.VEND_MASTERS_V vm
        INNER JOIN IMPERIAL.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
        INNER JOIN IMPERIAL.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
        LEFT OUTER JOIN IMPERIAL.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
        RIGHT OUTER JOIN IMPERIAL.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
        LEFT OUTER JOIN IMPERIAL.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
    WHERE        
        pm.CONTRACT IN ('1', '2', '6', '7')
        AND pa.EXPDATE IS NULL

    /* IHHMG */
    UNION ALL
    SELECT DISTINCT 
        pm.FIRSTNAME, 
        pm.LASTNAME, 
        pm.MI, 
        pm.FULLNAME, 
        pm.REV_FULLNAME, 
        pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
        pm.FROMDATE, 
        pm.TERMDATE, 
        ps.SPECCODE, 
        ps.SPECDESCR, 
        pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
        vm.VENDORNM, 
        pv.THRUDATE, 
        vm.VENDORNM1, 
        vm.VENDORNM2, 
        pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
        pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
        pa.EXPDATE, 
        pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
    FROM IHHMG.dbo.VEND_MASTERS_V vm
        INNER JOIN IHHMG.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
        INNER JOIN IHHMG.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
        LEFT OUTER JOIN IHHMG.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
        RIGHT OUTER JOIN IHHMG.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
        LEFT OUTER JOIN IHHMG.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
    WHERE        
        pm.CONTRACT IN ('1', '2', '6', '7')
        AND pa.EXPDATE IS NULL

    /* H2793 */
    UNION ALL
    SELECT DISTINCT 
        pm.FIRSTNAME, 
        pm.LASTNAME, 
        pm.MI, 
        pm.FULLNAME, 
        pm.REV_FULLNAME, 
        pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
        pm.FROMDATE, 
        pm.TERMDATE, 
        ps.SPECCODE, 
        ps.SPECDESCR, 
        pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
        vm.VENDORNM, 
        pv.THRUDATE, 
        vm.VENDORNM1, 
        vm.VENDORNM2, 
        pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
        pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
        pa.EXPDATE, 
        pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
    FROM H2793.dbo.VEND_MASTERS_V vm
        INNER JOIN H2793.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
        INNER JOIN H2793.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
        LEFT OUTER JOIN H2793.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
        RIGHT OUTER JOIN H2793.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
        LEFT OUTER JOIN H2793.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
    WHERE        
        pm.CONTRACT IN ('1', '2', '6', '7')
        AND pa.EXPDATE IS NULL
'''

qry_member = '''
    /* IICT */
    SELECT        
        mc.MEMB_KEYID, 
        mc.MEMB_MPI_NO, 
        mc.MEMBID COLLATE SQL_Latin1_General_CP1_CI_AS AS MID, 
        mc.COMPANY_ID, 
        mc.HPCODE COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr2, 
        mc.SSN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr3, 
        mc.PATID COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr4, 
        mc.LTRSENT, 
        mc.LTRDATE, 
        mc.LOADDATE, 
        mc.XPDATE, 
        mc.XPSTATUS COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr5, 
        mc.XPTRAN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr6, 
        mc.OUTLOADDT, 
        mc.Student, 
        mc.RLSHIP, 
        mc.CONTRACTS, 
        mc.STATUS, 
        mc.OTHPRIM, 
        mc.OTHNAME COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr7, 
        mc.OTHCOV, 
        mc.CREATEBY, 
        mc.CREATEDATE, 
        mc.LASTCHANGEBY, 
        mc.LASTCHANGEDATE, 
        mc.ePost_ITS1 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr8, 
        mc.ePost_ITS2 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr9, 
        mc.ePost_ITS3 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr10, 
        mc.ePost_ITS4 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr11, 
        mc.HoldCodeID, 
        mc.FAMILYNO, 
        mc.MEMBEPOSTITS, 
        mc.ISEZNET1, 
        mc.ISEZNET2, 
        mc.ISEZNET3, 
        mc.ISEZNET4, 
        mc.ISHPGLOBAL, 
        mc.MEMBINDIVIDUALDEATH, 
        mc.MEMBGROUP, 
        mc.POLICYREFERENCEID, 
        mc.DATETIMEQUAL, 
        mc.COVERAGELEVELCODE, 
        mh.OPTHRUDT, 
        mi.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS Zip, 
        mi.ADDRESSTYPE
    FROM IICT.dbo.MEMB_COMPANY mc
        INNER JOIN IICT.dbo.MEMB_HPHISTS_V mh ON mh.MEMB_KEYID = mc.MEMB_KEYID 
        INNER JOIN IICT.dbo.MEMB_CONTACT_INFORMATION mi ON mi.MEMB_KEYID = mc.MEMB_KEYID
    WHERE
        mh.OPTHRUDT IS NULL
        AND mi.ADDRESSTYPE='home'

    /* IMPERIAL */
    UNION ALL
    SELECT        
        mc.MEMB_KEYID, 
        mc.MEMB_MPI_NO, 
        mc.MEMBID COLLATE SQL_Latin1_General_CP1_CI_AS AS MID, 
        mc.COMPANY_ID, 
        mc.HPCODE COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr2, 
        mc.SSN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr3, 
        mc.PATID COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr4, 
        mc.LTRSENT, 
        mc.LTRDATE, 
        mc.LOADDATE, 
        mc.XPDATE, 
        mc.XPSTATUS COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr5, 
        mc.XPTRAN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr6, 
        mc.OUTLOADDT, 
        mc.Student, 
        mc.RLSHIP, 
        mc.CONTRACTS, 
        mc.STATUS, 
        mc.OTHPRIM, 
        mc.OTHNAME COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr7, 
        mc.OTHCOV, 
        mc.CREATEBY, 
        mc.CREATEDATE, 
        mc.LASTCHANGEBY, 
        mc.LASTCHANGEDATE, 
        mc.ePost_ITS1 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr8, 
        mc.ePost_ITS2 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr9, 
        mc.ePost_ITS3 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr10, 
        mc.ePost_ITS4 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr11, 
        mc.HoldCodeID, 
        mc.FAMILYNO, 
        mc.MEMBEPOSTITS, 
        mc.ISEZNET1, 
        mc.ISEZNET2, 
        mc.ISEZNET3, 
        mc.ISEZNET4, 
        mc.ISHPGLOBAL, 
        mc.MEMBINDIVIDUALDEATH, 
        mc.MEMBGROUP, 
        mc.POLICYREFERENCEID, 
        mc.DATETIMEQUAL, 
        mc.COVERAGELEVELCODE, 
        mh.OPTHRUDT, 
        mi.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS Zip, 
        mi.ADDRESSTYPE
    FROM IMPERIAL.dbo.MEMB_COMPANY mc
        INNER JOIN IMPERIAL.dbo.MEMB_HPHISTS_V mh ON mh.MEMB_KEYID = mc.MEMB_KEYID 
        INNER JOIN IMPERIAL.dbo.MEMB_CONTACT_INFORMATION mi ON mi.MEMB_KEYID = mc.MEMB_KEYID
    WHERE
        mh.OPTHRUDT IS NULL
        AND mi.ADDRESSTYPE='home'

    /* IHHMG */
    UNION ALL
    SELECT        
        mc.MEMB_KEYID, 
        mc.MEMB_MPI_NO, 
        mc.MEMBID COLLATE SQL_Latin1_General_CP1_CI_AS AS MID, 
        mc.COMPANY_ID, 
        mc.HPCODE COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr2, 
        mc.SSN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr3, 
        mc.PATID COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr4, 
        mc.LTRSENT, 
        mc.LTRDATE, 
        mc.LOADDATE, 
        mc.XPDATE, 
        mc.XPSTATUS COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr5, 
        mc.XPTRAN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr6, 
        mc.OUTLOADDT, 
        mc.Student, 
        mc.RLSHIP, 
        mc.CONTRACTS, 
        mc.STATUS, 
        mc.OTHPRIM, 
        mc.OTHNAME COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr7, 
        mc.OTHCOV, 
        mc.CREATEBY, 
        mc.CREATEDATE, 
        mc.LASTCHANGEBY, 
        mc.LASTCHANGEDATE, 
        mc.ePost_ITS1 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr8, 
        mc.ePost_ITS2 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr9, 
        mc.ePost_ITS3 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr10, 
        mc.ePost_ITS4 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr11, 
        mc.HoldCodeID, 
        mc.FAMILYNO, 
        mc.MEMBEPOSTITS, 
        mc.ISEZNET1, 
        mc.ISEZNET2, 
        mc.ISEZNET3, 
        mc.ISEZNET4, 
        mc.ISHPGLOBAL, 
        mc.MEMBINDIVIDUALDEATH, 
        mc.MEMBGROUP, 
        mc.POLICYREFERENCEID, 
        mc.DATETIMEQUAL, 
        mc.COVERAGELEVELCODE, 
        mh.OPTHRUDT, 
        mi.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS Zip, 
        mi.ADDRESSTYPE
    FROM IHHMG.dbo.MEMB_COMPANY mc
        INNER JOIN IHHMG.dbo.MEMB_HPHISTS_V mh ON mh.MEMB_KEYID = mc.MEMB_KEYID 
        INNER JOIN IHHMG.dbo.MEMB_CONTACT_INFORMATION mi ON mi.MEMB_KEYID = mc.MEMB_KEYID
    WHERE
        mh.OPTHRUDT IS NULL
        AND mi.ADDRESSTYPE='home'

    /* H2793 */
    UNION ALL
    SELECT        
        mc.MEMB_KEYID, 
        mc.MEMB_MPI_NO, 
        mc.MEMBID COLLATE SQL_Latin1_General_CP1_CI_AS AS MID, 
        mc.COMPANY_ID, 
        mc.HPCODE COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr2, 
        mc.SSN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr3, 
        mc.PATID COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr4, 
        mc.LTRSENT, 
        mc.LTRDATE, 
        mc.LOADDATE, 
        mc.XPDATE, 
        mc.XPSTATUS COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr5, 
        mc.XPTRAN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr6, 
        mc.OUTLOADDT, 
        mc.Student, 
        mc.RLSHIP, 
        mc.CONTRACTS, 
        mc.STATUS, 
        mc.OTHPRIM, 
        mc.OTHNAME COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr7, 
        mc.OTHCOV, 
        mc.CREATEBY, 
        mc.CREATEDATE, 
        mc.LASTCHANGEBY, 
        mc.LASTCHANGEDATE, 
        mc.ePost_ITS1 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr8, 
        mc.ePost_ITS2 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr9, 
        mc.ePost_ITS3 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr10, 
        mc.ePost_ITS4 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr11, 
        mc.HoldCodeID, 
        mc.FAMILYNO, 
        mc.MEMBEPOSTITS, 
        mc.ISEZNET1, 
        mc.ISEZNET2, 
        mc.ISEZNET3, 
        mc.ISEZNET4, 
        mc.ISHPGLOBAL, 
        mc.MEMBINDIVIDUALDEATH, 
        mc.MEMBGROUP, 
        mc.POLICYREFERENCEID, 
        mc.DATETIMEQUAL, 
        mc.COVERAGELEVELCODE, 
        mh.OPTHRUDT, 
        mi.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS Zip, 
        mi.ADDRESSTYPE
    FROM H2793.dbo.MEMB_COMPANY mc
        INNER JOIN H2793.dbo.MEMB_HPHISTS_V mh ON mh.MEMB_KEYID = mc.MEMB_KEYID 
        INNER JOIN H2793.dbo.MEMB_CONTACT_INFORMATION mi ON mi.MEMB_KEYID = mc.MEMB_KEYID
    WHERE
        mh.OPTHRUDT IS NULL
        AND mi.ADDRESSTYPE='home'
'''
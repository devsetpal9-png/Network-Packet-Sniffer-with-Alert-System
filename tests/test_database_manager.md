
### test_database_manager.py
```
test_database_initialization (test_database_manager.TestDatabaseManager) ... ok
test_insert_packet (test_database_manager.TestDatabaseManager) ... ok
test_insert_packet_partial_data (test_database_manager.TestDatabaseManager) ... ok
test_get_recent_packets (test_database_manager.TestDatabaseManager) ... ok
test_database_file_creation (test_database_manager.TestDatabaseManager) ... ok
test_invalid_db_path (test_database_manager.TestDatabaseManagerEdgeCases) ... ok
test_concurrent_access (test_database_manager.TestDatabaseManagerEdgeCases) ... ok
```

**Missing Lines:**
- Line 102: Very specific timing edge case

### src/database_manager.py




#ifndef _CAPPENDVFS_H
#define _CAPPENDVFS_H

#include "sqlite3.h"

#ifdef __cplusplus
extern "C" {
#endif

int sqlite3_appendvfs_init(sqlite3*, char**, const sqlite3_api_routines*);

#ifdef __cplusplus
}  /* end of the 'extern "C"' block */
#endif

#endif /* ifndef _APPENDVFS_H */
  
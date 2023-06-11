


#ifndef _CQPVTAB_H
#define _CQPVTAB_H

#include "sqlite3.h"

#ifdef __cplusplus
extern "C" {
#endif

int sqlite3_qpvtab_init(sqlite3*, char**, const sqlite3_api_routines*);

#ifdef __cplusplus
}  /* end of the 'extern "C"' block */
#endif

#endif /* ifndef _QPVTAB_H */
  
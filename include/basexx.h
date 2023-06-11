


#ifndef _CBASEXX_H
#define _CBASEXX_H

#include "sqlite3.h"

#ifdef __cplusplus
extern "C" {
#endif

int sqlite3_basexx_init(sqlite3*, char**, const sqlite3_api_routines*);

#ifdef __cplusplus
}  /* end of the 'extern "C"' block */
#endif

#endif /* ifndef _BASEXX_H */
  
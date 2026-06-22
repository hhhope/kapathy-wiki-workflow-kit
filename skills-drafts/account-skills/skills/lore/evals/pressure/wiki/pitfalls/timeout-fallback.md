# Pitfall — timeout-fallback

Keywords: timeout, fallback, hanging provider, worker backlog, external timeout, 超时降级, 外部依赖超时

External calls without explicit timeout and fallback stall workers and create retry backlog.

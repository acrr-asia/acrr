# Vietnamese translation guide

ACRR is published in English (the original) and Vietnamese (translations). This file is the
contract for every Vietnamese translation: where files go, what must stay identical to the
English original, and how technical terms are written. It is for authors and translators, not
for visitors.

## Files

| Content | English original | Vietnamese translation | Public URL |
|---|---|---|---|
| Article | `src/content/blog/<slug>.mdx` | `src/content/blog/vi/<slug>.mdx` | `/vi/blog/<slug>` |
| Series | `src/content/series/<id>.md` | `src/content/series/vi/<id>.md` | `/vi/series/<id>` |
| Insight | `src/content/insights/<id>.md` | `src/content/insights/vi/<id>.md` | `/vi/insights/<id>` |
| Learning item | `src/data/learning.json` | the item's optional `vi` object in the same file | `/vi/learning` |
| Interface text | `src/i18n/ui.ts` (`en`) | `src/i18n/ui.ts` (`vi`) | every `/vi/...` page |

A translation has the same file name (slug or id) as its original; the build fails if a
translation has no original. An untranslated article or insight still appears in Vietnamese
listings, marked as English and linking to the English page.

## What stays identical to the original

Frontmatter, except `title` and `description` (and, for a series, `objectives` and the titles and
descriptions of `plannedEntries`), is copied unchanged: `publishedAt`, `updatedAt`, `category`,
`tags`, `series`, `seriesOrder`, `status`, `kind`, `draft`, `example`. A series translation must
list the same number of planned entries, in the same order, and have the same `status` as the
original (the build checks both), so when an English series file changes, its translation must
change with it.

Also unchanged: every formula and number, code blocks, units and their symbols, figure
components and their props other than `caption`, reference lists (titles of cited works stay in
their original language), and the structure (same sections, same numbering, same tables).

In an `.mdx` translation, imports point one directory further up:
`import Figure from '../../../components/Figure.astro';`.

Links to another article point to its Vietnamese version (`/vi/blog/<slug>`) only when that
translation exists; otherwise they keep the English URL. Do not link to in-page anchors of a
translated page: Vietnamese headings produce different anchors from the English ones.

Mermaid diagrams are translated (node and edge labels); the generated SVG diagrams in
`src/components/diagrams/` keep their English labels for now, and their Vietnamese captions say
what the figure shows.

## Style

- Natural, precise technical Vietnamese, as in a good Vietnamese university textbook; not a
  word-for-word rendering of the English sentence structure. Keep the meaning, the order of ideas
  and every technical claim exactly.
- **Terms:** on its first use in each article, write the Vietnamese term followed by the English
  term in parentheses, for example *cầu Wheatstone (Wheatstone bridge)*, *độ không đảm bảo đo
  (measurement uncertainty)*; afterwards use the Vietnamese term alone. Keep standard acronyms as
  they are (ADC, DAC, SAR, CMRR, JWT, OAuth, HTTP, TLS, PID) and expand them in Vietnamese on first
  use, for example *bộ chuyển đổi tương tự – số (analog-to-digital converter, ADC)*. Where no
  established Vietnamese term exists, keep the English term in italics.
- **Numbers:** keep the decimal point used in the original (`0.385 Ω/°C`, `2.5 mV`) so prose,
  tables and formulas agree; separate thousands with a thin space as the original does
  (`65 536`). Units and symbols follow SI and are not translated.
- Section labels in summaries and tables are translated; table structure is unchanged.
- "Entry" (a part of a series) is *bài*; "the previous entry" is *bài trước*, "the next entry"
  *bài tiếp theo*, "the first entry" *bài thứ nhất*.

## Glossary

Use these renderings so that terms agree across articles.

| English | Tiếng Việt |
|---|---|
| measurement, measurand | phép đo, đại lượng cần đo |
| sensor, transducer | cảm biến, bộ chuyển đổi |
| measurement chain | chuỗi đo |
| sensing element | phần tử cảm biến |
| signal conditioning | chuẩn hóa tín hiệu (signal conditioning) |
| modulating / self-generating sensor | cảm biến điều chế / cảm biến tự phát |
| excitation | nguồn kích thích |
| sensitivity, resolution, accuracy, precision | độ nhạy, độ phân giải, độ chính xác, độ chụm |
| linearity, nonlinearity | độ tuyến tính, độ phi tuyến |
| hysteresis, drift, repeatability | độ trễ (hysteresis), độ trôi, độ lặp lại |
| range, span, full scale | dải đo, khoảng đo, toàn thang |
| error (systematic / random) | sai số (hệ thống / ngẫu nhiên) |
| uncertainty (standard / combined / expanded) | độ không đảm bảo đo (chuẩn / tổng hợp / mở rộng) |
| coverage factor | hệ số phủ |
| calibration, traceability | hiệu chuẩn, tính liên kết chuẩn |
| influence quantity | đại lượng ảnh hưởng |
| loading (effect) | hiệu ứng tải |
| time constant, bandwidth, cut-off frequency | hằng số thời gian, băng thông, tần số cắt |
| step response, frequency response | đáp ứng bước, đáp ứng tần số |
| strain gauge, gauge factor | cảm biến biến dạng (strain gauge), hệ số gauge |
| thermocouple, cold junction | cặp nhiệt điện, mối nối lạnh |
| resistance thermometer (PT100) | nhiệt điện trở bạch kim (PT100) |
| thermistor | nhiệt điện trở bán dẫn (thermistor) |
| photodiode, responsivity | điốt quang, độ đáp ứng |
| Wheatstone bridge, quarter / half / full bridge | cầu Wheatstone, cầu một phần tư / nửa cầu / cầu đủ |
| operational amplifier (op-amp) | bộ khuếch đại thuật toán (op-amp) |
| instrumentation amplifier | bộ khuếch đại đo lường (instrumentation amplifier) |
| common-mode / differential-mode | chế độ chung / chế độ vi sai |
| common-mode rejection ratio (CMRR) | tỉ số nén tín hiệu đồng pha (CMRR) |
| virtual ground | đất ảo |
| transimpedance amplifier | bộ khuếch đại xuyên trở (transimpedance amplifier) |
| charge amplifier | bộ khuếch đại điện tích |
| gain–bandwidth product | tích độ lợi – băng thông |
| offset voltage, bias current | điện áp lệch, dòng phân cực |
| low-pass filter, order | bộ lọc thông thấp, bậc |
| sampling, sampling frequency | lấy mẫu, tần số lấy mẫu |
| aliasing, alias, anti-aliasing filter | chồng phổ (aliasing), thành phần chồng phổ, bộ lọc chống chồng phổ |
| Nyquist frequency, sampling theorem | tần số Nyquist, định lý lấy mẫu |
| quantization, quantization step, LSB | lượng tử hóa, bước lượng tử, LSB |
| analog-to-digital converter (ADC) | bộ chuyển đổi tương tự – số (ADC) |
| digital-to-analog converter (DAC) | bộ chuyển đổi số – tương tự (DAC) |
| successive approximation, delta-sigma | xấp xỉ liên tiếp, delta-sigma |
| oversampling, decimation | lấy mẫu vượt mức, giảm tốc độ mẫu (decimation) |
| noise (thermal, shot, flicker), interference | nhiễu (nhiệt, bắn, nhấp nháy 1/f), can nhiễu |
| robot, degree of freedom | robot, bậc tự do |
| coordinate frame, transformation | hệ tọa độ, phép biến đổi |
| forward / inverse kinematics | động học thuận / động học ngược |
| state estimation, Kalman filter | ước lượng trạng thái, bộ lọc Kalman |
| feedback, controller, plant | phản hồi, bộ điều khiển, đối tượng điều khiển |
| authentication, authorization | xác thực, phân quyền |
| token, session, cookie | token, phiên, cookie |
| load cell | cảm biến lực (load cell) |
| voltage divider | mạch phân áp |
| dummy gauge | cảm biến biến dạng bù (dummy gauge) |
| voltage follower (buffer) | mạch lặp điện áp (mạch đệm) |
| difference / differential amplifier | bộ khuếch đại hiệu / bộ khuếch đại vi sai |
| ratiometric (measurement) | phép đo tỉ lệ (ratiometric) |
| notch filter, active filter | bộ lọc chắn dải hẹp (notch filter), bộ lọc tích cực |
| synchronous demodulator | bộ giải điều chế đồng bộ |
| galvanic isolation | cách ly galvanic |
| magnitude response | đáp ứng biên độ |
| energy domain | miền năng lượng |
| dark current, quantum efficiency | dòng tối, hiệu suất lượng tử |
| eddy current, magnetoresistive | dòng xoáy, từ trở |
| trueness, cross-sensitivity | độ đúng, độ nhạy chéo |
| threshold, dead band | ngưỡng, vùng chết |
| damping ratio, natural frequency | hệ số tắt dần, tần số dao động riêng |
| actuator | cơ cấu chấp hành |
| noise shaping, zero-order hold | định dạng nhiễu, giữ bậc không |
| reconstruction filter | bộ lọc khôi phục |
| offset error, gain error, missing code | sai số lệch không, sai số độ lợi, mã bị thiếu |
| aperture jitter | độ rung pha khẩu độ (aperture jitter) |
| dither | dither (kept in English) |
| digital twin, fieldbus | bản sao số, bus trường |
| verification, validation | kiểm chứng, thẩm định |

### Access control and security

| English | Tiếng Việt |
|---|---|
| access control | kiểm soát truy cập (access control) |
| identification, authentication, authorization, audit | định danh, xác thực, phân quyền, kiểm toán |
| reference monitor | bộ giám sát tham chiếu (reference monitor) |
| subject, object, action | chủ thể, đối tượng, hành động |
| principal | *principal* (kept in English; first use explains it as an entity that can be authenticated) |
| identifier | định danh |
| credential, authenticator | thông tin xác thực (credential), phương tiện xác thực (authenticator) |
| claimant, verifier | bên yêu cầu xác thực (claimant), bên xác minh (verifier) |
| claim | claim (kept in English; first use: *khẳng định (claim)*) |
| client, confidential / public client | client (kept), client bảo mật (confidential client) / client công khai (public client) |
| resource, resource server, resource owner | tài nguyên, máy chủ tài nguyên (resource server), chủ sở hữu tài nguyên (resource owner) |
| identity provider (IdP) | nhà cung cấp danh tính (identity provider, IdP) |
| authorization server | máy chủ phân quyền (authorization server) |
| relying party | bên tin cậy (relying party) |
| workload | *workload* (kept in English; software acting on its own behalf) |
| access token, refresh token, ID token | access token, refresh token, ID token (kept in English) |
| bearer token, sender-constrained token | bearer token (kept), token ràng buộc bên gửi (sender-constrained token) |
| self-contained token, opaque token | token tự chứa (self-contained token), token mờ (opaque token) |
| scope, consent | phạm vi (scope), sự đồng ý (consent) |
| grant, authorization code | luồng cấp quyền (grant), mã ủy quyền (authorization code) |
| endpoint | điểm cuối (endpoint) |
| delegation, delegated authorization | ủy nhiệm, phân quyền ủy nhiệm (delegated authorization) |
| federation, federated authentication, single sign-on | liên kết danh tính (federation), xác thực liên kết (federated authentication), đăng nhập một lần (single sign-on, SSO) |
| session, session identifier, session record | phiên (session), định danh phiên, bản ghi phiên |
| multi-factor authentication | xác thực đa yếu tố (multi-factor authentication, MFA) |
| one-time password, passkey | mật khẩu dùng một lần (one-time password, OTP), passkey (kept) |
| phishing, phishing resistance | lừa đảo giả mạo (phishing), khả năng chống phishing |
| cross-site scripting, cross-site request forgery | tấn công chèn mã độc liên trang (cross-site scripting, XSS), giả mạo yêu cầu liên trang (cross-site request forgery, CSRF) |
| signature, sign, verify | chữ ký, ký, xác minh |
| symmetric / asymmetric algorithm, key rotation | thuật toán đối xứng / bất đối xứng, xoay vòng khóa (key rotation) |
| expiry, revocation, introspection | hết hạn, thu hồi (revocation), kiểm tra trạng thái token (introspection) |
| staleness window | khoảng hiệu lực lỗi thời (staleness window) |
| allow-list, denylist | danh sách cho phép (allow-list), danh sách chặn (denylist) |
| clock skew | độ lệch đồng hồ (clock skew) |
| least privilege, complete mediation, fail-safe defaults | đặc quyền tối thiểu (least privilege), kiểm soát toàn diện (complete mediation), mặc định an toàn (fail-safe defaults) |
| policy enforcement point / decision point | điểm thực thi chính sách (PEP) / điểm quyết định chính sách (PDP) |
| access control list, capability | danh sách kiểm soát truy cập (access control list, ACL), năng lực (capability) |
| role-, attribute-, relationship-based access control | kiểm soát truy cập dựa trên vai trò (RBAC) / thuộc tính (ABAC) / quan hệ (ReBAC) |
| tenant | tổ chức thuê (tenant) |
| audit log | nhật ký kiểm toán (audit log) |
| request, response, header field, status code, body | yêu cầu, phản hồi, trường tiêu đề (header field), mã trạng thái, thân (body) |
| mutual TLS | TLS hai chiều (mutual TLS, mTLS) |
| proof of possession | bằng chứng sở hữu (proof of possession) |

HTTP method names, header names, cookie attributes, claim names, parameter names, error codes
and status phrases (`401 Unauthorized`) are code and stay in English.

### Robotics, control and numerical methods

| English | Tiếng Việt |
|---|---|
| link, joint, end effector | khâu, khớp, khâu tác động cuối (end effector) |
| workspace, singularity | không gian làm việc, điểm kỳ dị (singularity) |
| rotation matrix, homogeneous transformation | ma trận quay, phép biến đổi thuần nhất (homogeneous transformation) |
| Euler angles, gimbal lock, quaternion | góc Euler, khóa gimbal (gimbal lock), quaternion |
| Jacobian | ma trận Jacobi (Jacobian) |
| open loop, closed loop | vòng hở, vòng kín |
| gain, disturbance, setpoint / reference | độ lợi, nhiễu loạn (disturbance), giá trị đặt (setpoint) |
| overshoot, settling time, steady-state error | độ vọt lố (overshoot), thời gian xác lập, sai số xác lập |
| transfer function, pole, eigenvalue | hàm truyền, điểm cực (pole), trị riêng |
| state-space model, state vector | mô hình không gian trạng thái (state-space model), vector trạng thái |
| stability, stable, unstable | ổn định, ổn định, không ổn định |
| observer, odometry, dead reckoning | bộ quan sát (observer), đo hành trình (odometry), định vị suy đoán (dead reckoning) |
| sensor fusion, measurement update, prediction | hợp nhất cảm biến (sensor fusion), bước cập nhật đo, bước dự đoán |
| numerical integration, step size | tích phân số, bước thời gian (step size) |
| explicit / implicit method, stiff | phương pháp hiển / ẩn, hệ cứng (stiff) |
| truncation error, round-off error, floating point | sai số cắt cụt, sai số làm tròn, dấu phẩy động (floating point) |
| simulation, sim-to-real gap | mô phỏng, khoảng cách mô phỏng – thực tế (sim-to-real gap) |
| compute-bound, memory-bound, arithmetic intensity | bị giới hạn bởi tính toán (compute-bound), bị giới hạn bởi bộ nhớ (memory-bound), cường độ số học (arithmetic intensity) |

### Parallel and high-performance computing

| English | Tiếng Việt |
|---|---|
| parallel computing, high-performance computing (HPC) | tính toán song song, tính toán hiệu năng cao (high-performance computing, HPC) |
| processor, core, thread, process, node | bộ xử lý, lõi (core), luồng (thread), tiến trình (process), nút (node) |
| speedup, efficiency, scalability | hệ số tăng tốc (speedup), hiệu suất song song (efficiency), khả năng mở rộng (scalability) |
| strong scaling, weak scaling | mở rộng mạnh (strong scaling), mở rộng yếu (weak scaling) |
| Amdahl's law, Gustafson's law, serial fraction | định luật Amdahl, định luật Gustafson, tỉ lệ tuần tự (serial fraction) |
| work, span, parallelism | khối lượng công việc (work), độ dài đường găng (span), độ song song (parallelism) |
| roofline model, ridge point, peak performance | mô hình roofline (roofline model), điểm gãy (ridge point), hiệu năng đỉnh |
| bandwidth, latency, throughput | băng thông, độ trễ (latency), thông lượng |
| memory hierarchy, cache, cache line, cache miss | phân cấp bộ nhớ (memory hierarchy), bộ nhớ đệm (cache), dòng cache (cache line), trượt cache (cache miss) |
| locality (temporal / spatial), blocking (tiling) | tính cục bộ (thời gian / không gian), chia khối (blocking, tiling) |
| associativity, set, way | độ kết hợp (associativity), tập (set), đường (way) |
| prefetching, translation lookaside buffer (TLB) | nạp trước (prefetching), bộ đệm dịch địa chỉ (translation lookaside buffer, TLB) |
| array of structures, structure of arrays | mảng cấu trúc (array of structures, AoS), cấu trúc mảng (structure of arrays, SoA) |
| shared memory, distributed memory | bộ nhớ dùng chung (shared memory), bộ nhớ phân tán (distributed memory) |
| data race, race condition, atomic operation | tranh chấp dữ liệu (data race), điều kiện tranh chấp (race condition), thao tác nguyên tử (atomic operation) |
| mutual exclusion, lock, critical section, barrier | loại trừ lẫn nhau, khóa (lock), đoạn găng (critical section), rào chắn (barrier) |
| memory consistency model, memory ordering | mô hình nhất quán bộ nhớ (memory consistency model), thứ tự bộ nhớ (memory ordering) |
| false sharing, load imbalance, scheduling | chia sẻ giả (false sharing), mất cân bằng tải (load imbalance), lập lịch (scheduling) |
| reduction | phép rút gọn (reduction) |
| vector instruction, SIMD, lane | lệnh vector, SIMD, làn (lane) |
| graphics processing unit (GPU), kernel, warp, thread block | bộ xử lý đồ họa (graphics processing unit, GPU), kernel (kept), warp (kept), khối luồng (thread block) |
| coalescing, divergence, occupancy, offloading | gộp truy cập bộ nhớ (coalescing), phân kỳ (divergence), độ lấp đầy (occupancy), chuyển tải tính toán (offloading) |
| message passing, point-to-point, collective operation | truyền thông điệp (message passing), truyền điểm – điểm (point-to-point), thao tác tập thể (collective operation) |
| domain decomposition, halo (ghost) cells, halo exchange | phân rã miền (domain decomposition), ô biên ảo (halo cells), trao đổi biên (halo exchange) |
| broadcast, all-reduce | phát quảng bá (broadcast), all-reduce (kept) |

### Motion planning

| English | Tiếng Việt |
|---|---|
| motion planning, path planning, planner | lập kế hoạch chuyển động (motion planning), lập kế hoạch đường đi (path planning), bộ lập kế hoạch (planner) |
| configuration, configuration space, free space, obstacle region | cấu hình, không gian cấu hình (configuration space), không gian tự do (free space), vùng vật cản (obstacle region) |
| workspace, obstacle | không gian làm việc, vật cản |
| Minkowski sum | tổng Minkowski (Minkowski sum) |
| path, trajectory, time scaling, waypoint | đường đi (path), quỹ đạo (trajectory), tham số hóa thời gian (time scaling), điểm trung gian (waypoint) |
| collision checking, clearance | kiểm tra va chạm (collision checking), khoảng hở an toàn (clearance) |
| complete, resolution complete, probabilistically complete, asymptotically optimal | đầy đủ (complete), đầy đủ theo độ phân giải (resolution complete), đầy đủ theo xác suất (probabilistically complete), tối ưu tiệm cận (asymptotically optimal) |
| graph, node (vertex), edge, cost | đồ thị, đỉnh (node), cạnh, chi phí |
| graph search, Dijkstra's algorithm, A*, heuristic, admissible, consistent | tìm kiếm trên đồ thị, thuật toán Dijkstra, A*, hàm heuristic (heuristic), chấp nhận được (admissible), nhất quán (consistent) |
| open list, closed list, priority queue | danh sách mở (open list), danh sách đóng (closed list), hàng đợi ưu tiên (priority queue) |
| occupancy grid, cell, connectivity | lưới chiếm dụng (occupancy grid), ô, tính liên thông (4-/8-connectivity) |
| sampling-based planning, probabilistic roadmap (PRM), rapidly-exploring random tree (RRT) | lập kế hoạch dựa trên lấy mẫu (sampling-based planning), bản đồ lộ trình xác suất (probabilistic roadmap, PRM), cây ngẫu nhiên khám phá nhanh (rapidly-exploring random tree, RRT) |
| narrow passage, steering function, nearest neighbor | lối đi hẹp (narrow passage), hàm lái (steering function), lân cận gần nhất (nearest neighbor) |
| shortcutting, smoothing | rút ngắn đường đi (shortcutting), làm trơn (smoothing) |
| velocity profile, trapezoidal profile, S-curve, jerk | biên dạng vận tốc (velocity profile), biên dạng hình thang, biên dạng chữ S (S-curve), độ giật (jerk) |
| cubic / quintic polynomial, spline | đa thức bậc ba / bậc năm, spline (kept) |
| path tracking, pure pursuit, look-ahead distance | bám đường đi (path tracking), thuật toán pure pursuit (kept), khoảng nhìn trước (look-ahead distance) |
| differential-drive robot, unicycle model | robot dẫn động vi sai (differential-drive robot), mô hình unicycle (kept) |
| potential field, local minimum, dynamic window approach | trường thế (potential field), cực tiểu cục bộ, phương pháp cửa sổ động (dynamic window approach, DWA) |
| replanning, global / local planner | lập lại kế hoạch (replanning), bộ lập kế hoạch toàn cục / cục bộ |

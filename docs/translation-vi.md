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
translation has no original. The one exception is a **Vietnamese original**: an article written in
Vietnamese first, at the user's request, while its English version is still planned. It lives in
`src/content/blog/vi/<slug>.mdx` with `originalLang: "vi"` in its frontmatter, appears only in
Vietnamese listings and routes, and its series' English file lists it under `plannedEntries` while
the Vietnamese file does not (the build checks that the English planned count equals the Vietnamese
count plus the series' Vietnamese originals, and allows the two `status` values to differ). When the
English version is written, remove `originalLang` from the Vietnamese file and the planned entry
from the English series file; from then on it is an ordinary translation. An untranslated article or insight still appears in Vietnamese
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

### Critical thinking and logic

"Bias" in data or sampling is *sai lệch*; *thiên kiến* is kept for cognitive biases. Link texts that
name another entry of the series use that entry's Vietnamese title (the part before the colon).

| English | Tiếng Việt |
|---|---|
| critical thinking, reasoning | tư duy phản biện (critical thinking), lập luận |
| claim, statement, proposition | nhận định, phát biểu (statement), mệnh đề (proposition) |
| meaning, ambiguity, vagueness | ý nghĩa, tính mơ hồ (ambiguity), tính không rõ ranh giới (vagueness) |
| definition, necessary / sufficient condition | định nghĩa, điều kiện cần / điều kiện đủ |
| argument, premise, conclusion | lập luận (argument), tiền đề (premise), kết luận (conclusion) |
| hidden assumption, argument map, principle of charity | giả định ẩn (hidden assumption), sơ đồ lập luận (argument map), nguyên tắc thiện chí |
| deductive, inductive, analogical argument | lập luận diễn dịch, lập luận quy nạp, lập luận loại suy |
| valid, sound, inductively strong, cogent | hợp lệ (valid), đúng đắn (sound), mạnh về quy nạp (inductively strong), thuyết phục (cogent) |
| consistency, contradiction, logical form, self-defeating | tính nhất quán, mâu thuẫn, hình thức logic (logical form), tự bác bỏ |
| contrary / contradictory, logical truth, topic neutrality, logically equivalent | đối chọi / mâu thuẫn, chân lý logic, tính trung lập về chủ đề, tương đương logic |
| entailment, logical consequence, counterexample | kéo theo (entailment), hệ quả logic, phản ví dụ (counterexample) |
| categorical logic / statement / syllogism, subject / predicate term | logic định danh, mệnh đề định danh (categorical statement), tam đoạn luận định danh, thuật ngữ chủ ngữ / vị ngữ |
| major / minor / middle term, distribution, universe of discourse | thuật ngữ lớn / nhỏ / giữa, chu diên, miền thảo luận |
| undistributed middle, illicit major / minor, exclusive premises, existential fallacy | thuật ngữ giữa không chu diên, mở rộng bất hợp lệ thuật ngữ lớn / nhỏ, hai tiền đề phủ định, ngụy biện tồn tại |
| Venn diagram, existential import, conversion, contraposition | biểu đồ Venn, hàm ý tồn tại (existential import), phép đảo (mệnh đề đảo), phép phản đảo (mệnh đề phản đảo) |
| sentential (propositional) logic, connective, well-formed formula (WFF) | logic mệnh đề (sentential logic), liên từ logic (connective), công thức đúng cú pháp (well-formed formula, WFF) |
| negation, conjunction, disjunction (inclusive / exclusive), conditional, biconditional | phủ định, hội (conjunction), tuyển (disjunction; bao hàm / loại trừ), điều kiện (conditional), song điều kiện (biconditional) |
| material conditional, antecedent, consequent, only if, unless | điều kiện vật chất (material conditional), tiền kiện (antecedent), hậu kiện (consequent), chỉ khi, trừ khi |
| truth table, truth value, truth-functional, assignment | bảng chân trị, giá trị chân lý, hàm chân trị, phép gán (assignment) |
| tautology, contradiction, contingent | hằng đúng (tautology), hằng sai (contradiction), khả biến (contingent) |
| affirming the consequent, denying the antecedent | khẳng định hậu kiện, phủ định tiền kiện |
| hypothetical / disjunctive syllogism, constructive dilemma, modus ponens / tollens | tam đoạn luận giả định / tam đoạn luận tuyển, song đề kiến tạo, modus ponens / modus tollens (kept) |
| natural deduction, derivation, rule of inference, derived rule, discharge | suy diễn tự nhiên (natural deduction), dẫn xuất (derivation), quy tắc suy luận, quy tắc phái sinh (derived rule), giải phóng (giả định) |
| soundness, completeness (of a proof system), decidable | tính đúng đắn (soundness), tính đầy đủ (completeness), khả quyết |
| predicate logic, quantifier (universal / existential), variable, domain | logic vị từ (predicate logic), lượng từ (toàn thể / tồn tại), biến, miền (domain) |
| interpretation, model, counter-model, extension | diễn giải (interpretation), mô hình (model), phản mô hình (counter-model), ngoại diên (extension) |
| hypothesis, test implication, auxiliary hypothesis, hypothetico-deductive method | giả thuyết, hệ quả kiểm tra, giả thuyết phụ trợ, phương pháp giả thuyết – diễn dịch |
| confirm / disconfirm, falsifiability, burden of proof, Occam's razor | xác nhận / làm suy yếu, tính khả bác bỏ (falsifiability), nghĩa vụ chứng minh, dao cạo Occam |
| correlation, association, causation, confounder, controlled experiment | tương quan, mối liên hệ, quan hệ nhân quả, biến gây nhiễu (confounder), thí nghiệm có đối chứng |
| INUS condition, causal field, standing condition, trigger, mechanism | điều kiện INUS, trường nhân quả, điều kiện thường trực, yếu tố kích hoạt, cơ chế |
| Mill's methods: agreement, difference, joint method, residues, concomitant variations | phương pháp tương đồng, khác biệt, kết hợp, phần dư, biến thiên đồng hành |
| causal network, chain / fork / collider, mediator, fishbone diagram | mạng nhân quả, chuỗi / rẽ nhánh / hội tụ, biến trung gian, biểu đồ xương cá |
| randomization, A/B test, blind / double-blind, placebo, observational study | ngẫu nhiên hóa, kiểm thử A/B, mù / mù đôi, giả dược, nghiên cứu quan sát |
| probability, conditional probability, odds, mutually exclusive, addition / multiplication rule | xác suất, xác suất có điều kiện, tỉ số cược, xung khắc, quy tắc cộng / quy tắc nhân |
| base rate, prior, likelihood, posterior, likelihood ratio, false-positive rate, natural frequencies | tỉ lệ nền (base rate), tiên nghiệm, hàm hợp lý, hậu nghiệm, tỉ số hợp lý, tỉ lệ dương tính giả, tần số tự nhiên |
| sample, population, sampling / selection / survivorship / publication bias | mẫu, tổng thể, sai lệch chọn mẫu / sai lệch chọn lọc / sai lệch kẻ sống sót / sai lệch công bố |
| sampling error, standard error, margin of error, confidence interval | sai số chọn mẫu, sai số chuẩn, biên sai số, khoảng tin cậy |
| statistical significance, p-value, null / alternative hypothesis, Type I / II error, power | ý nghĩa thống kê, giá trị p (p-value), giả thuyết không / giả thuyết đối, sai lầm loại I / II, lực kiểm định |
| regression to the mean, Simpson's paradox | hồi quy về giá trị trung bình, nghịch lý Simpson |
| value judgment, descriptive / normative claim, thick ethical concept | phán đoán giá trị (value judgment), nhận định mô tả / nhận định chuẩn tắc, khái niệm đạo đức dày |
| instrumental / intrinsic value, means / end | giá trị công cụ / giá trị nội tại, phương tiện / mục đích |
| is-ought gap, bridging premise, naturalistic fallacy | khoảng cách giữa "là" và "nên", tiền đề bắc cầu, ngụy biện tự nhiên chủ nghĩa |
| moral relativism / absolutism / contextualism, reflective equilibrium, formal justice | thuyết tương đối / thuyết tuyệt đối / thuyết ngữ cảnh đạo đức, cân bằng phản tư, công bằng hình thức |
| utility, utilitarianism, virtue ethics | độ hữu dụng, thuyết vị lợi, đạo đức học đức hạnh |
| Hohfeld: claim-right, duty, privilege, no-right, power, liability, immunity, disability | quyền yêu cầu, nghĩa vụ, đặc quyền, không-quyền, quyền năng, chịu tác động, quyền miễn trừ, vô năng |
| problem statement, decomposition, flowchart, swimlane flowchart | phát biểu vấn đề, phân rã, lưu đồ, lưu đồ làn bơi |
| decision matrix (weighted), expected value, SWOT analysis, 7-S framework | ma trận quyết định (có trọng số), giá trị kỳ vọng, phân tích SWOT, khung 7-S |
| payoff table, regret, minimax regret, decisions under uncertainty / risk | bảng lợi ích, độ hối tiếc, minimax hối tiếc, quyết định trong điều kiện bất định / rủi ro |
| decision tree, chance node, expected value of perfect information (EVPI) | cây quyết định, nút ngẫu nhiên, giá trị kỳ vọng của thông tin hoàn hảo (EVPI) |
| fallacy (formal / informal), cognitive bias | ngụy biện (hình thức / phi hình thức), thiên kiến nhận thức (cognitive bias) |
| begging the question, equivocation, straw man, red herring | lấy kết luận làm tiền đề, đánh tráo khái niệm, (ngụy biện) người rơm, đánh lạc hướng |
| false dilemma, loaded question, slippery slope, appeal to ignorance | song đề giả, câu hỏi đánh bẫy, dốc trượt, viện dẫn sự thiếu hiểu biết |
| gambler's fallacy, base-rate neglect, hasty generalization, quantifier shift | ngụy biện của người đánh bạc, bỏ qua tỉ lệ nền, khái quát hóa vội vàng, hoán vị lượng từ |
| heuristic (in judgment / in problem solving), availability, representativeness | lối tắt tư duy / gợi ý tìm tòi (heuristic), tính sẵn có, tính đại diện |
| anchoring, framing, confirmation / outcome / hindsight bias, planning / sunk cost fallacy | hiệu ứng mỏ neo, hiệu ứng khung, thiên kiến xác nhận / kết quả / nhìn lại, ngụy biện lập kế hoạch / chi phí chìm |
| creativity, divergent / convergent thinking (production) | sáng tạo, tư duy (tạo sinh) phân kỳ / hội tụ |
| incubation, fixation, functional fixedness | ấp ủ, sự cố định tư duy, sự cố định chức năng |
| brainstorming, production blocking, evaluation apprehension, groupthink | động não, tắc nghẽn tạo sinh, lo ngại bị đánh giá, tư duy nhóm |

### Bayesian deep learning

Calibration keeps the existing rendering *hiệu chuẩn* (first table); "calibrated" is *được hiệu
chuẩn*. "Mode" stays in English (not *mốt*). "Bias" of an estimator is *chệch* (*không chệch* for
unbiased), the bias parameter of a unit is *độ chệch (bias)*, and data bias follows the rule of the
Critical thinking section. "Precision" in the sense of inverse variance is *độ chính xác*, distinct
from the measurement sense *độ chụm*. In prose, "et al." is written *và cộng sự*.

| English | Tiếng Việt |
|---|---|
| Bayesian deep learning, Bayesian neural network, Bayesian model averaging | học sâu Bayes, mạng nơ-ron Bayes, lấy trung bình mô hình Bayes (Bayesian model averaging) |
| posterior predictive, prior predictive, marginal likelihood, evidence | phân phối dự đoán hậu nghiệm (posterior predictive), phân phối dự đoán tiên nghiệm (prior predictive), hàm hợp lý biên (marginal likelihood), bằng chứng (evidence) |
| MAP estimate, point estimate, weight decay, precision, prior precision | ước lượng hậu nghiệm cực đại (maximum a posteriori, MAP), ước lượng điểm, suy giảm trọng số (weight decay), độ chính xác (precision), độ chính xác tiên nghiệm |
| epistemic / aleatoric uncertainty, mutual information | độ bất định nhận thức / ngẫu nhiên (epistemic / aleatoric uncertainty), thông tin tương hỗ (mutual information) |
| mode, multimodal, mode connectivity, basin of attraction | mode (kept in English), đa mode, tính liên thông giữa các mode (mode connectivity), miền hút (basin of attraction) |
| approximate inference, ensemble, deep ensemble, member | suy luận xấp xỉ (approximate inference), tổ hợp mô hình (ensemble), tổ hợp sâu (deep ensemble), thành viên |
| Markov chain Monte Carlo, Hamiltonian Monte Carlo, stochastic-gradient MCMC | Monte Carlo xích Markov (Markov chain Monte Carlo, MCMC), Monte Carlo Hamilton (Hamiltonian Monte Carlo, HMC), MCMC gradient ngẫu nhiên (SG-MCMC) |
| Markov chain, stationary distribution, burn-in, effective sample size, detailed balance | xích Markov, phân phối dừng, giai đoạn khởi động (burn-in), cỡ mẫu hiệu dụng (effective sample size, ESS), cân bằng chi tiết |
| random walk, leapfrog integrator, (stochastic gradient) Langevin dynamics | bước ngẫu nhiên (random walk), bộ tích phân leapfrog, động lực học Langevin, động lực học Langevin gradient ngẫu nhiên (SGLD) |
| cold posterior, tempered posterior, temperature | hậu nghiệm lạnh (cold posterior), phân phối hậu nghiệm điều chỉnh nhiệt độ (tempered posterior), nhiệt độ |
| Laplace approximation, linearized predictive, generalized Gauss–Newton, K-FAC | xấp xỉ Laplace, phân phối dự đoán tuyến tính hóa, ma trận Gauss–Newton tổng quát (GGN), độ cong xấp xỉ phân tích Kronecker (K-FAC) |
| Hessian, (empirical) Fisher information matrix, factorization | ma trận Hesse (Hessian), ma trận thông tin Fisher (thực nghiệm), phép phân tích (Cholesky, Kronecker); eigendecomposition: phân rã trị riêng |
| variational inference, ELBO, mean-field, reparameterization trick, natural gradient | suy luận biến phân (VI), cận dưới của bằng chứng (ELBO), trường trung bình (mean-field), thủ thuật tái tham số hóa, gradient tự nhiên |
| Gaussian process, kernel, lengthscale, squared-exponential kernel, inducing points | quá trình Gauss (GP), hàm nhân (kernel), thang độ dài (lengthscale), hàm nhân mũ bình phương, điểm cảm sinh (inducing points) |
| NNGP, neural tangent kernel, deep kernel learning | quá trình Gauss của mạng nơ-ron (NNGP), hàm nhân tiếp tuyến nơ-ron (NTK), học hàm nhân sâu |
| weight-space symmetry, identifiability, (un)identifiable, label switching | đối xứng không gian trọng số, tính khả định danh (identifiability), (không) khả định danh, hoán đổi nhãn (label switching) |
| inductive bias | thiên hướng quy nạp (inductive bias) |
| last-layer inference, single-forward-pass method, feature collapse, distance-aware | suy luận lớp cuối, phương pháp một lượt truyền xuôi, sụp đổ đặc trưng (feature collapse), nhận biết khoảng cách (distance-aware) |
| proper / strictly proper scoring rule, log score, Brier score | quy tắc chấm điểm thích đáng (proper scoring rule) / thích đáng chặt, điểm log, điểm Brier |
| confidence, reliability diagram, expected calibration error, temperature scaling | độ tự tin (confidence), biểu đồ độ tin cậy (reliability diagram), sai số hiệu chuẩn kỳ vọng (ECE), co giãn nhiệt độ (temperature scaling) |
| selective classification / prediction, coverage, selective risk | phân loại / dự đoán có chọn lọc, độ phủ (coverage), rủi ro chọn lọc |
| active learning, acquisition function, BALD | học chủ động (active learning), hàm thu nhận (acquisition function), học chủ động Bayes qua bất đồng (BALD) |
| classifier, gradient descent, benchmark, validation set | bộ phân loại, hạ gradient, bộ dữ liệu chuẩn (benchmark), tập kiểm định |
| random seed, mini-batch, forward pass | hạt giống ngẫu nhiên (random seed), lô nhỏ (mini-batch), lượt truyền xuôi |
| prior-fitted network, singular learning theory | mạng khớp sẵn tiên nghiệm (prior-fitted network, PFN), lý thuyết học kỳ dị |
| Monte Carlo estimator, unbiased, consistent, canonical rate | ước lượng Monte Carlo, không chệch, vững (consistent), tốc độ chuẩn tắc (canonical rate) |
| rejection sampling, importance sampling, importance weight, self-normalized | lấy mẫu loại bỏ (rejection sampling), lấy mẫu quan trọng (importance sampling; not *lấy mẫu theo trọng số quan trọng*), trọng số quan trọng, tự chuẩn hóa (self-normalized) |
| proposal distribution / density, target distribution, acceptance rate | phân phối / mật độ đề xuất (proposal distribution / density), phân phối mục tiêu, tỉ lệ chấp nhận (acceptance rate) |
| transition kernel, Markov kernel, base kernel | nhân chuyển (transition kernel), nhân Markov (Markov kernel), nhân cơ sở; never *hạt nhân*; a GP or kernel-method kernel stays *hàm nhân* |
| mixing, ergodicity, invariance, irreducible, aperiodic, warm-up | trộn (mixing), tính ergodic (ergodicity), tính bất biến (invariance), tối giản (irreducible), không tuần hoàn (aperiodic), giai đoạn khởi động (warm-up, as for burn-in) |
| random-walk Metropolis, Metropolis-adjusted Langevin algorithm, Gibbs sampler | Metropolis bước ngẫu nhiên (random-walk Metropolis, RWM), thuật toán Langevin hiệu chỉnh Metropolis (MALA), bộ lấy mẫu Gibbs |
| step size, step-size schedule, cyclical | kích thước bước (step size; an integrator's time step $\Delta t$ stays *bước thời gian*), lịch kích thước bước, chu kỳ (cyclical: SG-MCMC chu kỳ, lịch chu kỳ; *tuần hoàn* only for periodic / aperiodic) |
| momentum, mass matrix, friction, overdamped / underdamped Langevin | động lượng (momentum), ma trận khối lượng (mass matrix), ma sát (friction), Langevin quá tắt dần / dưới tắt dần (overdamped / underdamped) |
| local, global, locally / globally balanced proposal | cục bộ (not *địa phương*), toàn cục, phân phối đề xuất cân bằng cục bộ / toàn cục |
| sequential Monte Carlo, particle, resampling, mutation, particle filter, SMC sampler | Monte Carlo tuần tự (sequential Monte Carlo, SMC), hạt (particle), tái lấy mẫu (resampling; not *lấy mẫu lại*), đột biến (mutation), bộ lọc hạt (particle filter), bộ lấy mẫu SMC |
| tempering, annealing, annealed importance sampling | điều chỉnh nhiệt độ (tempering), ủ nhiệt (annealing), lấy mẫu quan trọng có ủ nhiệt (annealed importance sampling, AIS) |
| credible set / interval | tập khả tín / khoảng khả tín (credible set / interval) |
| energy, energy landscape, energy-based model, partition function | năng lượng, cảnh quan năng lượng, mô hình dựa trên năng lượng (energy-based model), hàm phân hoạch (partition function) |
| simulation-based inference, simulator, neural posterior / likelihood / ratio estimation | suy luận dựa trên mô phỏng (SBI), bộ mô phỏng, ước lượng hậu nghiệm / hàm hợp lý / tỉ số bằng mạng nơ-ron (NPE / NLE / NRE) |
| normalizing flow, embedding network, summary statistic, amortized, coverage diagnostics, misspecification | luồng chuẩn hóa (normalizing flow), mạng nhúng (embedding network), thống kê tóm tắt, khấu hao (amortized), chẩn đoán độ phủ, đặc tả sai (misspecification) |
| multilevel Monte Carlo, telescoping sum, coupling, trace-class | Monte Carlo đa mức (MLMC), tổng lồng (telescoping sum), phép ghép cặp (coupling), lớp vết (trace-class) |
| low precision, quantization gap, stochastic / deterministic rounding, fixed point, gradient accumulator | độ chính xác thấp (low precision; numeric sense), khoảng cách lượng tử (quantization gap), làm tròn ngẫu nhiên / tất định, dấu phẩy tĩnh (fixed point), bộ tích lũy gradient |
| point estimate, curvature (of a Laplace approximation) | ước lượng điểm, độ cong |
| regularized empirical risk, regularizer, energy function | rủi ro thực nghiệm có chính quy hóa, số hạng chính quy hóa (regularizer), hàm năng lượng |
| linearized network, linearization point, network Jacobian | mạng tuyến tính hóa, điểm tuyến tính hóa, ma trận Jacobi của mạng (network Jacobian) |
| local minimizer / maximum / optimum | điểm cực tiểu / cực đại / tối ưu cục bộ (not *địa phương*) |
| post hoc | sau huấn luyện (post hoc); not *hậu kiểm* |
| pushforward (noun), push forward (verb) | ảnh đẩy tới (pushforward), đẩy tới |
| pullback (metric), pull back | metric kéo lùi (pullback), kéo lùi |
| matrix-free | không cần lập ma trận (matrix-free) |
| matrix-vector product, covariance-vector product | tích ma trận – vector, tích hiệp phương sai – vector |
| Kronecker-factored approximate curvature (KFAC / K-FAC), Kronecker factor | độ cong xấp xỉ phân tích Kronecker (KFAC; acronym spelled as in the original), thừa số Kronecker |
| diagonal / low-rank / block-diagonal approximation | xấp xỉ đường chéo / hạng thấp / đường chéo khối |
| eigenpair, top eigenspace, Woodbury matrix identity | cặp trị riêng – vector riêng (cặp riêng), không gian riêng trội, đẳng thức ma trận Woodbury |
| positive (semi)definite (PSD), rank-deficient, degenerate | (nửa) xác định dương (PSD), hụt hạng (thiếu hạng), suy biến |
| Kullback–Leibler (KL) divergence | độ phân kỳ Kullback–Leibler (KL) on first use per article, then *độ phân kỳ KL* |
| score (gradient of the log-likelihood), sufficient statistic | hàm điểm (score), thống kê đủ (sufficient statistic) |
| exponential family, natural parameter, partition function, base measure | họ mũ (exponential family), tham số tự nhiên, hàm phân hoạch, độ đo cơ sở |
| empirical Fisher (EFIM) | ma trận thông tin Fisher thực nghiệm (empirical Fisher, EFIM) |
| cross-entropy, softmax, logit, probit, link function | entropy chéo (cross-entropy), softmax, logit, probit, hàm liên kết |
| Riemannian metric, Fisher (information) metric, statistical manifold | metric Riemann (Riemannian metric), metric (thông tin) Fisher, đa tạp thống kê (statistical manifold) |
| tangent space, tangent vector, tangent kernel | không gian tiếp xúc (tangent space), vector tiếp tuyến, hàm nhân tiếp tuyến |
| fiber, fiber bundle, effective parameter space | thớ (fiber), phân thớ (fiber bundle), không gian tham số hiệu dụng |
| diffeomorphism, isometry, exponential map | vi phôi (diffeomorphism), phép đẳng cự (isometry), ánh xạ mũ (exponential map) |
| reparametrized / Riemannian / diffusion Laplace approximation | xấp xỉ Laplace tái tham số hóa / Riemann / khuếch tán |
| damping, preconditioner | số hạng tắt dần (damping), bộ tiền điều kiện (preconditioner) |
| gradient flow, gradient ascent | dòng gradient (gradient flow), leo gradient (gradient ascent) |
| overconfidence, asymptotic confidence | sự quá tự tin (overconfidence), độ tự tin tiệm cận |
| out-of-distribution (OOD), in-distribution (ID) | ngoài phân phối (out-of-distribution, OOD), trong phân phối (in-distribution, ID) |
| continual learning, catastrophic forgetting | học liên tục (continual learning), quên thảm họa (catastrophic forgetting) |
| elastic weight consolidation (EWC) | củng cố trọng số đàn hồi (elastic weight consolidation, EWC) |
| plasticity, stability, process noise, smoothing | tính dẻo (plasticity), tính ổn định (stability), nhiễu quá trình, làm trơn (smoothing) |
| Bayesian optimization, surrogate model, upper confidence bound (UCB) | tối ưu hóa Bayes (BO), mô hình thay thế (surrogate model), cận tin cậy trên (UCB) |
| information gain, expected predictive information gain (EPIG) | lượng thông tin thu được (information gain), lượng thông tin dự đoán thu được kỳ vọng (EPIG) |
| exploration, exploitation | khám phá (exploration), khai thác (exploitation) |
| model selection, hyperparameter, hyperprior | lựa chọn mô hình (model selection), siêu tham số (hyperparameter), siêu tiên nghiệm (hyperprior) |
| hierarchical Bayes, type-II maximum likelihood (ML-II) | Bayes phân cấp, hợp lý cực đại loại II (maximum likelihood II, ML-II) |
| Occam's razor, cross-validation | dao cạo Occam (Occam's razor), kiểm định chéo (cross-validation) |
| PAC-Bayes bound, sub-Gamma | cận PAC-Bayes, dưới Gamma (sub-Gamma) |
| online (model selection / optimization) | trực tuyến (online) |
| flat / sharp minimum, loss landscape | cực tiểu phẳng / nhọn (flat / sharp minimum), bề mặt hàm mất mát (loss landscape) |
| overfitting, underfitting | quá khớp (overfitting), chưa khớp (underfitting) |
| pruning (structured / unstructured), probing, invariance | tỉa (có cấu trúc / không cấu trúc), thăm dò (probing), tính bất biến (invariance) |
| variational family, variational parameters, factorized (distribution) | họ biến phân (variational family), tham số biến phân (variational parameters), (phân phối) phân tích thành tích |
| coordinate ascent variational inference (CAVI), conditionally conjugate | suy luận biến phân leo theo tọa độ (CAVI), liên hợp có điều kiện (conditionally conjugate) |
| forward / reverse KL, mode-seeking / mode-covering | KL thuận / KL ngược (forward / reverse KL), tìm mode / phủ mode (mode-seeking / mode-covering) |
| reparameterization gradient, pathwise estimator, score-function (REINFORCE) estimator | gradient tái tham số hóa, bộ ước lượng theo đường đi (pathwise estimator), bộ ước lượng hàm điểm (score-function estimator, REINFORCE) |
| doubly stochastic, control variate, variance reduction | ngẫu nhiên kép (doubly stochastic), biến điều khiển (control variate), giảm phương sai |
| variational autoencoder, encoder, decoder, inference network, amortized inference | bộ tự mã hóa biến phân (VAE), bộ mã hóa (encoder), bộ giải mã (decoder), mạng suy luận (inference network), suy luận khấu hao (amortized inference) |
| local latent variable, importance-weighted autoencoder (IWAE), Jensen's inequality | biến ẩn cục bộ, bộ tự mã hóa có trọng số quan trọng (IWAE), bất đẳng thức Jensen |
| moment matching, moment | khớp mô-men (moment matching; not *khớp mômen*), mô-men |
| stochastic regularization technique (SRT), dropout rate, dropout mask | kỹ thuật chính quy hóa ngẫu nhiên (SRT), tỉ lệ dropout (dropout rate), mặt nạ dropout (dropout mask) |
| Monte Carlo dropout, Concrete Dropout, dropout injection | dropout Monte Carlo (MC Dropout), Concrete Dropout (kept), chèn dropout (dropout injection) |
| continuous relaxation, Gumbel-softmax trick, Concrete distribution | phép nới lỏng liên tục (continuous relaxation), thủ thuật Gumbel-softmax, phân phối Concrete |
| scale factor, scale-agnostic / scale-aware, σ-scaling | hệ số co giãn (scale factor; *tỉ lệ* is reserved for the dropout rate), không xét / có xét co giãn, co giãn σ (σ-scaling) |
| generalized Bayes, generalized posterior, Gibbs posterior, variational learning | Bayes tổng quát (Generalized Bayes), hậu nghiệm tổng quát, hậu nghiệm Gibbs, học biến phân (variational learning) |
| Bayesian learning rule (BLR) | quy tắc học Bayes (Bayesian learning rule, BLR) |
| expectation parameter, mean parameter, dual (moment) parameters | tham số kỳ vọng (expectation parameter), tham số trung bình (mean parameter), tham số đối ngẫu (mô-men) (dual (moment) parameters) |
| minimal exponential family, log-partition function | họ mũ tối thiểu, hàm log phân hoạch (log-partition function) |
| variational online Newton (VON), variational online Gauss–Newton (VOGN), improved VON (IVON) | Newton trực tuyến biến phân (VON), Gauss–Newton trực tuyến biến phân (VOGN), Newton trực tuyến biến phân cải tiến (IVON) |
| Bonnet's theorem, Price's theorem, Stein's lemma | định lý Bonnet, định lý Price, bổ đề Stein |
| per-example gradients, gradient magnitude approximation, feasible set, delta method | gradient theo từng mẫu, xấp xỉ độ lớn gradient, tập khả thi (feasible set), phương pháp delta |
| particle-based variational inference (ParVI), Stein variational gradient descent (SVGD), Stein variational Newton (SVN) | suy luận biến phân dựa trên hạt (ParVI), hạ gradient biến phân Stein (SVGD), Newton biến phân Stein (SVN) |
| Stein operator, Stein's identity, Stein kernel, Stein witness function | toán tử Stein, đẳng thức Stein, hàm nhân Stein, hàm chứng Stein |
| discrepancy, Stein discrepancy, kernel Stein discrepancy (KSD), maximum mean discrepancy (MMD) | độ sai khác (discrepancy), độ sai khác Stein, độ sai khác Stein dựa trên hàm nhân (KSD), độ sai khác trung bình cực đại (MMD) |
| reproducing kernel Hilbert space (RKHS), reproducing property | không gian Hilbert hàm nhân tái sinh (RKHS), tính chất tái sinh |
| transport map, continuity equation, Fokker–Planck equation | ánh xạ vận chuyển (transport map), phương trình liên tục, phương trình Fokker–Planck |
| first / second variation, functional gradient, functional Hessian | biến phân thứ nhất / thứ hai, gradient hàm (functional gradient), ma trận Hesse hàm |
| Wasserstein / Stein / Fisher-Rao gradient flow, birth-death process | dòng gradient Wasserstein / Stein / Fisher-Rao, quá trình sinh-tử (birth-death process) |
| metric tensor, Onsager operator, cotangent space, local coordinate chart | tenxơ metric, toán tử Onsager, không gian đối tiếp xúc, bản đồ tọa độ cục bộ (not *địa phương*) |
| relative Fisher information, (Stein) log-Sobolev inequality, dissipation | thông tin Fisher tương đối, bất đẳng thức log-Sobolev (Stein), sự tiêu tán |
| descent lemma, propagation of chaos, mean-field / population limit | bổ đề giảm (descent lemma), sự lan truyền hỗn loạn (propagation of chaos), giới hạn trường trung bình / giới hạn quần thể |
| bandwidth, median heuristic, random Fourier features, variance collapse | độ rộng (bandwidth), quy tắc trung vị (median heuristic), đặc trưng Fourier ngẫu nhiên, sụp đổ phương sai (variance collapse) |
| unadjusted Langevin algorithm (ULA), Langevin Monte Carlo (LMC) | thuật toán Langevin không hiệu chỉnh (ULA), Monte Carlo Langevin (LMC) |
| well-posed / ill-posed | đặt chỉnh / đặt không chỉnh (well-posed / ill-posed) |
| function-space variational inference (FSVI), evaluation map, likelihood functional | suy luận biến phân trong không gian hàm (FSVI), ánh xạ định giá (evaluation map), phiếm hàm hợp lý |
| cylinder σ-algebra, Radon–Nikodym derivative, absolutely continuous, mutually singular | σ-đại số trụ, đạo hàm Radon–Nikodym, liên tục tuyệt đối, kỳ dị lẫn nhau (mutually singular) |
| data-processing inequality, Gaussian measure, Hilbert–Schmidt operator | bất đẳng thức xử lý dữ liệu, độ đo Gauss (Gaussian measure), toán tử Hilbert–Schmidt |
| generalized variational objective (GVO), surrogate objective | hàm mục tiêu biến phân tổng quát hóa (GVO), hàm mục tiêu thay thế |
| state-space model (SSM), belief state, filtering distribution | mô hình không gian trạng thái (SSM), trạng thái niềm tin (belief state), phân phối lọc |
| dynamics (transition) model, observation (measurement) model | mô hình động lực (mô hình chuyển trạng thái), mô hình quan sát (mô hình đo) |
| predict step, update step, innovation, Kalman gain, information form | bước dự đoán, bước cập nhật, phần đổi mới (innovation), độ lợi Kalman, dạng thông tin (information form) |
| extended Kalman filter (EKF), statistical linear regression (SLR), unscented / cubature KF | bộ lọc Kalman mở rộng (EKF), hồi quy tuyến tính thống kê (SLR), *Unscented* KF / KF cầu phương khối |
| Gaussian quadrature, plugin approximation | cầu phương Gauss (Gaussian quadrature), xấp xỉ thế trực tiếp (plugin) |
| assumed density filtering (ADF), expectation propagation (EP) | lọc mật độ giả định (ADF), lan truyền kỳ vọng (Expectation Propagation) |
| Bayesian online natural gradient (BONG), diagonal plus low rank (DLR) | gradient tự nhiên trực tuyến Bayes (BONG), đường chéo cộng hạng thấp (DLR) |
| system identification, empirical Bayes, mirror descent | nhận dạng hệ thống, Bayes thực nghiệm (empirical Bayes), hạ gương (mirror descent) |
| equally weighted (predictive) mixture, functionally distinct solutions | hỗn hợp (dự đoán) có trọng số bằng nhau, các nghiệm khác biệt về mặt hàm |
| basin (short for basin of attraction), single-basin / multi-basin | miền hút (basin), một miền hút / đa miền hút |
| high-fidelity reference, predictive marginalization | tham chiếu có độ trung thực cao, phép lấy biên dự đoán |
| model combination | kết hợp mô hình (model combination); distinct from *lấy trung bình mô hình Bayes* |
| stochastic weight averaging (SWA), SWAG, MultiSWAG | lấy trung bình trọng số ngẫu nhiên (Stochastic Weight Averaging, SWA), SWAG, MultiSWAG |
| snapshot ensemble, fast geometric ensembling, anchored ensemble, BatchEnsemble | tổ hợp ảnh chụp nhanh (snapshot ensemble), tổ hợp hình học nhanh (fast geometric ensembling), tổ hợp có neo (anchored ensemble), BatchEnsemble |
| wall-clock time | thời gian thực (wall-clock time) |
| initialization / discretization / Monte Carlo error | sai số khởi tạo / rời rạc hóa / Monte Carlo |
| typical set, posterior landscape, energy barrier | tập điển hình (typical set), cảnh quan hậu nghiệm, rào năng lượng (energy barrier) |
| hybrid sampling, optimization-based initialization | lấy mẫu lai, khởi tạo dựa trên tối ưu hóa |
| potential, drift, injected noise | thế năng (potential), số hạng trôi (drift), nhiễu được bơm vào |
| unadjusted Langevin algorithm, No-U-Turn Sampler (NUTS) | thuật toán Langevin không hiệu chỉnh (unadjusted Langevin algorithm), bộ lấy mẫu không quay đầu (No-U-Turn Sampler, NUTS) |
| Bayesian deep ensemble (BDE), pseudo-ensemble | tổ hợp sâu Bayes (BDE), giả tổ hợp (pseudo-ensemble) |
| stochastic localization, denoiser, score-based | định vị ngẫu nhiên (stochastic localization), bộ khử nhiễu (denoiser), dựa trên hàm điểm (score-based) |
| stacking | xếp chồng (stacking) |
| ensemble learning, ensemble pruning | học tổ hợp (ensemble learning), tỉa tổ hợp (ensemble pruning) |
| mixture of experts (MoE), expert, router, gating network, gating value | hỗn hợp chuyên gia (mixture of experts, MoE), chuyên gia, bộ định tuyến (router), mạng cổng (gating network), giá trị cổng |
| shared / routed expert, token-to-expert affinity | chuyên gia dùng chung / được định tuyến, độ tương hợp giữa token và chuyên gia (token-to-expert affinity) |
| routing diversity, routing collapse, load balancing, auxiliary loss | độ đa dạng định tuyến (routing diversity), sụp đổ định tuyến (routing collapse), cân bằng tải, mất mát phụ |
| active / activated parameters | tham số hoạt động / được kích hoạt |
| large language model (LLM), finetuning | mô hình ngôn ngữ lớn (large language model, LLM), tinh chỉnh (finetuning) |
| reinforcement learning (RL), RLHF, reward model, policy | học tăng cường (RL), học tăng cường từ phản hồi của con người (RLHF), mô hình phần thưởng (reward model), chính sách (policy) |
| model-based / model-free RL, offline / online RL, world model | RL dựa trên mô hình / không dựa trên mô hình, RL ngoại tuyến / trực tuyến, mô hình thế giới (world model) |
| rollout, trust region, sample complexity | lượt triển khai (rollout), vùng tin cậy, độ phức tạp mẫu (sample complexity) |
| relevance score, relevance accuracy / consistency | điểm liên quan (relevance score), độ chính xác / độ nhất quán liên quan |
| model checkpoint | điểm lưu mô hình (model checkpoint) |
| PAC-Bayesian analysis, frequentist | phân tích PAC-Bayes (PAC-Bayesian analysis), theo trường phái tần suất (frequentist) |
| "prior" / "posterior" (PAC-Bayes sense) | "tiên nghiệm" / "hậu nghiệm" (in quotation marks as in the original) |
| randomized classifier, (weighted) majority vote | bộ phân loại ngẫu nhiên hóa (randomized classifier), bỏ phiếu đa số (có trọng số) (weighted majority vote) |
| expected / empirical loss (risk), zero-one loss | mất mát (rủi ro) kỳ vọng / thực nghiệm, mất mát không – một (zero-one loss) |
| oracle bound, first / second order | cận oracle (oracle bound), bậc một / bậc hai |
| tandem loss, tandem classifier | mất mát cặp đôi (tandem loss), bộ phân loại cặp đôi |
| binary kl-divergence, PAC-Bayes-kl inequality | độ phân kỳ kl nhị phân (binary kl-divergence), bất đẳng thức PAC-Bayes-kl |
| change of measure inequality, union bound | bất đẳng thức đổi độ đo (change of measure inequality), cận hợp (union bound) |
| (refined) Pinsker's, Jensen's, (second order) Markov's, Chebyshev-Cantelli inequality | bất đẳng thức Pinsker (tinh chỉnh), Jensen, Markov (bậc hai), Chebyshev-Cantelli |
| tight / loose bound, slack, fast / slow rate | cận chặt / lỏng, độ hở, tốc độ nhanh / chậm |
| cancellation of errors (effect) | hiệu ứng triệt tiêu sai số |
| alternating minimization, (strongly) quasi-convex | cực tiểu hóa luân phiên (alternating minimization), tựa lồi (mạnh) |
| bagging, out-of-bag samples | bagging, mẫu ngoài túi (out-of-bag) |
| moment (of a distribution), moment matching | mô-men (not *mômen*), khớp mô-men |
| prior elicitation, domain knowledge | khơi gợi tiên nghiệm (prior elicitation; not *thu thập*), tri thức về lĩnh vực |
| informative / uninformative / weakly informative prior | tiên nghiệm có thông tin (informative prior; not *giàu thông tin*) / không thông tin (not *không mang thông tin*) / ít thông tin |
| objective / subjective prior, reference prior, Jeffreys prior | tiên nghiệm khách quan / chủ quan, tiên nghiệm tham chiếu (reference prior), tiên nghiệm Jeffreys |
| conjugate prior, base prior | tiên nghiệm liên hợp (conjugate prior), tiên nghiệm cơ sở (base prior) |
| improper / proper (prior, posterior) | không chính thường (improper) / chính thường |
| prior predictive check, prior misspecification | phép kiểm tra dự đoán tiên nghiệm (prior predictive check), đặc tả sai tiên nghiệm |
| regularization prior, convenience prior | tiên nghiệm chính quy hóa, tiên nghiệm tiện lợi (convenience prior) |
| sparsity-inducing prior, soft / hard sparsity, (continuous) shrinkage prior | tiên nghiệm tạo tính thưa (not *thúc đẩy tính thưa*), tính thưa mềm / cứng, tiên nghiệm co (liên tục) |
| spike-and-slab prior, horseshoe prior, half-Cauchy | tiên nghiệm spike-and-slab, tiên nghiệm horseshoe (names kept in English, not italicized), nửa Cauchy (half-Cauchy) |
| scale mixture (of Gaussians), scale parameter | hỗn hợp co giãn (của phân phối Gauss) (scale mixture), tham số co giãn (scale parameter); not *thang đo*, which stays for a measurement scale |
| heavy-tailed / light-tailed, tail parameter / index | đuôi nặng (heavy tail; not *đuôi dày*) / đuôi nhẹ, tham số đuôi / chỉ số đuôi |
| inclusion probability, variable selection, median probability model | xác suất đưa vào (inclusion probability), chọn biến (variable selection), mô hình xác suất trung vị |
| point mass, Dirac delta | khối lượng điểm (point mass), delta Dirac |
| induce, induced (prior, distribution) | cảm sinh (not *tạo ra* in this sense), tiên nghiệm / phân phối được cảm sinh |
| over-parameterized, over-parameterization | quá tham số hóa |
| kernel density estimate (plot) | (đồ thị) ước lượng mật độ hàm nhân (kernel density estimate) |
| pre-activation, post-activation | tiền kích hoạt (pre-activation), hậu kích hoạt (post-activation; not *sau kích hoạt*) |
| sub-Gaussian, sub-exponential, sub-Weibull, Weibull tail | dưới Gauss, dưới mũ, dưới Weibull (as for sub-Gamma), đuôi Weibull |
| Meijer G-function | hàm G Meijer (Meijer G-function) |
| infinite-width / infinite-depth limit, finite-width regime | giới hạn độ rộng vô hạn / độ sâu vô hạn, chế độ độ rộng hữu hạn |
| α-stable prior, stable process, spectral measure | tiên nghiệm α-ổn định, quá trình ổn định, độ đo phổ (spectral measure) |
| trace-class prior, extended envelope property | tiên nghiệm lớp vết, tính chất bao mở rộng (extended envelope property) |
| Student-t process, Gaussian-Inverse-Gamma prior | quá trình Student-t, tiên nghiệm Gauss–Gamma nghịch đảo |
| Bayesian asymptotics, posterior consistency, (statistical) adaptation | tiệm cận Bayes, tính vững của hậu nghiệm (posterior consistency), sự thích nghi (thống kê) |
| posterior contraction rate, near-minimax rate | tốc độ co của hậu nghiệm (contraction rate), tốc độ gần minimax |
| Bernstein–von Mises (BvM) theorem | định lý Bernstein–von Mises (BvM) |
| kurtosis, excess kurtosis | độ nhọn (kurtosis), độ nhọn dư |
| function-space prior, weight-space / parameter-space prior | tiên nghiệm trong không gian hàm (function-space prior), tiên nghiệm trong không gian trọng số / tham số |
| neural process, finite-dimensional marginals, Kolmogorov extension theorem | quá trình nơ-ron (neural process), các phân phối biên hữu hạn chiều, định lý mở rộng Kolmogorov |
| exchangeable / exchangeability, consistency (of a process) | khả hoán / tính khả hoán (exchangeability), tính nhất quán (consistency; an estimator's *consistent* stays *vững*) |
| change of variables | phép đổi biến (change of variables) |
| integral probability metric, Wasserstein distance, Earth-Mover distance | metric xác suất tích phân (integral probability metric), khoảng cách Wasserstein, khoảng cách Earth-Mover |
| Lipschitz function, gradient penalty, measurement points | hàm 1-Lipschitz, số hạng phạt gradient (gradient penalty), điểm đo (measurement points) |
| fan-in scaling | co giãn theo số đầu vào (fan-in); not *chia tỉ lệ* |
| context data / inputs, context inference problem, context observation model | dữ liệu / đầu vào ngữ cảnh, bài toán suy luận ngữ cảnh, mô hình quan sát ngữ cảnh |
| cost function, uncertainty-aware / group-aware prior, group robustness | hàm chi phí (cost function), tiên nghiệm nhận biết độ bất định / nhận biết nhóm, tính vững theo nhóm (group robustness) |
| sharpness-aware minimization (SAM), stop-gradient, surrogate gradient | cực tiểu hóa nhận biết độ nhọn (SAM), toán tử dừng gradient (stop-gradient), gradient thay thế |
| residual connection, receptive field, neural ODE | kết nối phần dư (residual connection), trường tiếp nhận (receptive field), ODE nơ-ron (neural ODE) |
| Lemma | Bổ đề |
| Takeaways (box label) | Điểm cần ghi nhớ |
| Equation N, Proposition, Definition, Theorem, Proof, Figure, Table, Algorithm | Phương trình N, Mệnh đề, Định nghĩa, Định lý, Chứng minh, Hình, Bảng, Thuật toán |
| link text "Chapter K, Section j" | Chương K, Mục j (link to `/vi/blog/<slug>` without the `#` anchor) |
| kernel method, kernel trick, kernelized, kernel machine | phương pháp hàm nhân (kernel methods), thủ thuật hàm nhân (kernel trick), hàm nhân hóa (kernelized), máy hàm nhân (kernel machine) |
| feature map, feature space, input space | ánh xạ đặc trưng (feature map), không gian đặc trưng, không gian đầu vào |
| Gram matrix, kernel matrix | ma trận Gram, ma trận hàm nhân |
| positive (semi-)definite kernel, strictly positive definite | hàm nhân (nửa) xác định dương, xác định dương chặt |
| covariance function, mean function | hàm hiệp phương sai, hàm trung bình |
| linear / polynomial / Matérn / Laplacian / periodic / arc-cosine kernel | hàm nhân tuyến tính / đa thức / Matérn / Laplace / tuần hoàn / arc-cos |
| radial basis function (RBF) kernel | hàm nhân hàm cơ sở bán kính (radial basis function, RBF) on first use, then *hàm nhân RBF* |
| squared exponential (SE) / exponentiated quadratic kernel | hàm nhân mũ bình phương for both English names (they are the same kernel; not *mũ bậc hai*) |
| stationary / isotropic kernel, non-stationarity | hàm nhân dừng / đẳng hướng, tính không dừng |
| spectral density, Bochner's theorem, spectral-mixture kernel | mật độ phổ, định lý Bochner, hàm nhân hỗn hợp phổ |
| universal / characteristic kernel, mean embedding | hàm nhân phổ quát / đặc trưng hóa, phép nhúng trung bình |
| Representer theorem, Moore-Aronszajn theorem | định lý biểu diễn, định lý Moore-Aronszajn |
| expressiveness, expressive (power) | sức biểu đạt, giàu sức biểu đạt (not *khả năng biểu diễn*, which collides with representation) |
| composition, compose, process composition | hợp thành, phép hợp thành, hợp thành quá trình (not *ghép*); composed function: hàm hợp |
| inducing input / variable / value / feature, interdomain | đầu vào / biến / giá trị / đặc trưng cảm sinh, liên miền (interdomain) |
| sparse GP, sparse variational GP (SVGP) | GP thưa, GP biến phân thưa (sparse variational GP) |
| deep kernel, deep kernel GP | hàm nhân sâu, GP với hàm nhân sâu (quá trình Gauss với hàm nhân sâu) |
| feature extractor, base kernel (of a deep kernel) | bộ trích xuất đặc trưng (feature extractor), hàm nhân cơ sở (base kernel) |
| stochastic variational deep kernel learning (SVDKL), structured kernel interpolation (SKI, KISS-GP) | học hàm nhân sâu biến phân ngẫu nhiên (SVDKL), nội suy hàm nhân có cấu trúc (SKI) |
| deep Gaussian process (deep GP, DGP) | quá trình Gauss sâu (GP sâu, DGP) |
| warping, input warping, warped GP | sự uốn (warping), uốn đầu vào, GP uốn (warped GP) |
| bottleneck (layer), layer collapse | (lớp) nút cổ chai (bottleneck), sụp đổ lớp (layer collapse) |
| explicit-latent / implicit-latent view | góc nhìn biến ẩn tường minh / ngầm định |
| GP-LVM, hierarchical GP-LVM | GP-LVM (kept), GP-LVM phân cấp |
| restricted Boltzmann machine, deep belief network, contrastive divergence | máy Boltzmann giới hạn (RBM), mạng niềm tin sâu (deep belief network), phân kỳ tương phản (contrastive divergence) |
| collapsed / uncollapsed bound, variational compression | cận thu gọn / không thu gọn, nén biến phân |
| doubly stochastic variational inference (DSVI), psi-statistics | suy luận biến phân ngẫu nhiên kép (DSVI), thống kê psi |
| inference scheme, variational scheme | lược đồ suy luận, lược đồ biến phân (not *sơ đồ* or *cơ chế*) |
| automatic relevance determination (ARD) | xác định mức liên quan tự động (ARD) |
| "Schematic reproduction" (figure caption) | Bản tái hiện dạng sơ đồ |
| deep kernel process (DKP), deep kernel machine (DKM) | quá trình hàm nhân sâu (DKP), máy hàm nhân sâu (DKM) |
| Wishart distribution, scale matrix, degrees of freedom | phân phối Wishart, ma trận co giãn (scale matrix), bậc tự do |
| deep (inverse) Wishart process (DWP / DIWP), (generalized) singular Wishart | quá trình Wishart (nghịch đảo) sâu, Wishart suy biến (tổng quát) |
| permutation symmetry | đối xứng hoán vị |
| Bayesian representation learning limit (BRLL), DKM objective | giới hạn học biểu diễn Bayes (BRLL), hàm mục tiêu DKM |
| preactivation, postactivation | tiền kích hoạt, hậu kích hoạt |
| partitioned Gaussian, prior conditional | Gauss phân khối (partitioned Gaussian), tiên nghiệm có điều kiện |
| (Bayesian) model mismatch | đặc tả sai mô hình (Bayes) |
| meta-learning, meta-learned, meta-training, meta-testing, meta-dataset | siêu học (meta-learning), được siêu học, siêu huấn luyện, siêu kiểm tra, siêu tập dữ liệu |
| few-shot learning, support set, query set | học với ít mẫu (few-shot learning), tập hỗ trợ (support set), tập truy vấn (query set) |
| single-task / multi-task (learning, GP) | đơn tác vụ / đa tác vụ |
| bilevel optimization, inner optimization, hypergradient | tối ưu hóa hai cấp (bilevel optimization), tối ưu hóa bên trong, siêu gradient (hypergradient) |
| implicit function theorem (IFT), implicit differentiation | định lý hàm ẩn (IFT), vi phân ẩn |
| deep kernel transfer (DKT), ADKF-IFT | chuyển giao hàm nhân sâu (DKT), ADKF-IFT (name kept; glossed as *khớp hàm nhân sâu thích nghi bằng định lý hàm ẩn*) |
| instantiation (of a framework) | hiện thực (instantiation) |
| negative log marginal likelihood (NLML), negative log likelihood (NLL) | logarit âm của hàm hợp lý biên (NLML), logarit âm của hàm hợp lý (NLL) |
| out-of-domain, in-domain | ngoài miền (out-of-domain, OOD), trong miền; distinct from out-of-distribution (*ngoài phân phối*) |
| baseline, molecular fingerprint | phương pháp cơ sở (baseline), dấu vân tay phân tử (molecular fingerprint) |

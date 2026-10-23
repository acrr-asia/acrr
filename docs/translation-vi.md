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
